import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_tshark_decimal_sampling_intervals():
    module = load('observability_tshark_metrics')
    assert module.parse_io_stats('| 0.000 <> 1.000 | 12 | 2400 |\n| 1 <> 2 | 3 | 600 |') == (15, 3000)


def test_checksum_paths_follow_current_project():
    module = load('observability_prom_config_checksum')
    monkey_root = pathlib.Path(module.get_obs_base())
    assert all(pathlib.Path(p).is_relative_to(monkey_root) for p in module.FILES)
    assert all('Anish-DevOps-Lab' not in p for p in module.FILES)


def test_unprivileged_thermal_state(monkeypatch, tmp_path):
    module = load('observability_cpu_fan_metrics')
    monkeypatch.setattr(module, 'OUTFILE', str(tmp_path / 'thermal.prom'))
    monkeypatch.setattr(module, 'run_powermetrics_plist', lambda: b'')
    class Result:
        stdout = '2\n'
    monkeypatch.setattr(module.subprocess, 'run', lambda *args, **kwargs: Result())
    module.main()
    data = (tmp_path / 'thermal.prom').read_text()
    assert 'cpu_thermal_pressure_level 2' in data
    assert 'cpu_thermal_pressure_state{state="Heavy"} 1' in data
    assert 'cpu_temperature_available 0' in data


def test_dashboard_ids_sources_and_missing_data():
    def panels(items):
        for panel in items:
            yield panel
            yield from panels(panel.get('panels', []))
    for file in (ROOT.parent / 'grafana/dashboards').glob('*.json'):
        data = json.loads(file.read_text())
        items = list(panels(data['panels']))
        ids = [p['id'] for p in items]
        assert len(ids) == len(set(ids)), file.name
        for panel in items:
            for target in panel.get('targets', []):
                expr = target.get('expr', '')
                assert 'system_kv' not in expr or 'mac_system_kv' in expr
                assert '\\"' not in expr
                if 'count_over_time' not in expr:
                    assert 'or on() vector(0)' not in expr
                source = target.get('datasource') or panel.get('datasource')
                if isinstance(source, dict):
                    assert source['uid'] in ('PBFA97CFB590B2093', 'observatory-loki')


def test_environment_infers_checkout_path(monkeypatch, tmp_path):
    config = tmp_path / '.env'
    config.write_text('TEXTFILE_DIR="${OBS_BASE}/node_exporter/textfile"\n')
    monkeypatch.setenv('OBS_ENV_FILE', str(config))
    monkeypatch.delenv('OBS_BASE', raising=False)
    monkeypatch.delenv('TEXTFILE_DIR', raising=False)
    module = load('observability_env')
    module.load_env()
    assert pathlib.Path(module.get_obs_base()) == ROOT.parent
    assert pathlib.Path(module.get_textfile_dir()) == ROOT.parent / 'node_exporter/textfile'
