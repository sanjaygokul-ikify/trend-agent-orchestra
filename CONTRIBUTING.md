# Contributing to AgentOrchestra

## Development Setup
1. `git clone https://github.com/yourorg/agent-orchestra.git`
2. `make setup`
3. `make lint-fix`

## Code Style
- Use 4-space indentation
- Type hints required on all public APIs
- Add test coverage for new features

## Testing
Run full suite with:
bash
make test
# Or specific component:
pytest tests/consensus


## Issue Workflow
1. Create minimal repro case
2. Include network topology details
3. Attach wire logs if available

## Code of Conduct
All contributors must follow our strict anti-harassment policy.