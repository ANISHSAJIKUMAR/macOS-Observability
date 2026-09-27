# Contributing to macOS Observatory

First off, thank you for considering contributing to macOS Observatory! 🎉

## 🌟 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **macOS version** and **hardware specs**
- **Logs** from relevant services

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Include:

- **Clear title and description**
- **Use case** - why is this valuable?
- **Proposed solution** (if you have one)
- **Alternative solutions** you've considered

### Pull Requests

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test on macOS (ideally multiple versions)
5. Commit with clear messages (`git commit -m 'Add: New battery metric exporter'`)
6. Push to your branch
7. Open a Pull Request

## 📝 Style Guide

### Shell Scripts

- Use `#!/usr/bin/env bash` or `#!/bin/bash`
- Add descriptive comments
- Use meaningful variable names
- Test with `shellcheck`

### Python Scripts

- Follow PEP 8
- Add docstrings
- Use type hints where appropriate
- Test with `pylint` or `flake8`

### Commit Messages

Format: `Type: Brief description`

Types:
- `Add:` New feature
- `Fix:` Bug fix
- `Update:` Enhancement to existing feature
- `Docs:` Documentation changes
- `Refactor:` Code refactoring
- `Test:` Adding tests

Examples:
```
Add: CPU temperature metric exporter
Fix: Prometheus path configuration on fresh install
Update: README with better installation instructions
Docs: Add troubleshooting section for Grafana
```

## 🧪 Testing

Before submitting a PR:

- [ ] Test setup script on clean macOS
- [ ] Verify all services start successfully
- [ ] Check Grafana dashboards load
- [ ] Confirm metrics are collected
- [ ] Test on at least macOS 12+

## 🎨 Adding New Exporters

To add a custom macOS metric exporter:

1. Create script in `observability/exporters/`
2. Follow naming: `observability_{name}_metrics.py`
3. Output Prometheus format
4. Create LaunchAgent plist
5. Document metrics in `METRICS_CATALOG.md`
6. Update README

Example structure:
```python
#!/usr/bin/env python3
"""
Description of what this exporter does
"""

def collect_metrics():
    """Collect and return metrics in Prometheus format"""
    return "my_metric{label=\"value\"} 42\n"

if __name__ == "__main__":
    print(collect_metrics())
```

## 📊 Adding Grafana Dashboards

1. Create dashboard in Grafana
2. Export JSON
3. Save to `observability/grafana/dashboards/`
4. Document in README
5. Include screenshot

## 🐛 Debug Checklist

When debugging issues:

- Check service status: `brew services list`
- View Prometheus errors: `tail -50 /opt/homebrew/var/log/prometheus.err.log`
- Check Grafana logs: `tail -50 /opt/homebrew/var/log/grafana.log`
- Test Prometheus config: `promtool check config prometheus.yml`
- Verify ports: `lsof -i :9090`

## 💡 Ideas for Contributions

### Easy (Good First Issues)

- Add more alert rule examples
- Improve documentation
- Add more PromQL query examples
- Create simple Grafana dashboards

### Medium

- New macOS metric exporters
- Enhanced dashboard templates
- Automated testing scripts
- Docker support

### Advanced

- Kubernetes integration
- Remote storage support
- Advanced alerting rules
- Performance optimizations

## 🔒 Security

Found a security issue? Please email privately rather than opening a public issue.

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🤝 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks
- Trolling or insulting comments
- Publishing others' private information

## ❓ Questions?

- Open an issue with label `question`
- Check existing documentation
- Review closed issues

## 🎉 Recognition

Contributors will be:
- Listed in README
- Mentioned in release notes
- Thanked in commit messages

Thank you for making this project better! 🚀
