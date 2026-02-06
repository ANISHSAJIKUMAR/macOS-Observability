import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_exporters_have_expected_structure():
    exporters = sorted(ROOT.glob("observability_*.py"))
    assert exporters, "No exporters found"

    for path in exporters:
        text = path.read_text(encoding="utf-8")
        assert text.startswith("#!/usr/bin/env python3") or text.startswith(
            "#!/usr/bin/env python"
        )
        assert "get_textfile_dir" in text, f"missing get_textfile_dir in {path.name}"
        assert ".prom" in text, f"missing .prom output in {path.name}"


def test_env_helpers_default_paths():
    env = ROOT / "observability_env.py"
    assert env.exists()
    text = env.read_text(encoding="utf-8")
    assert "get_textfile_dir" in text
