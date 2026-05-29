# oracle_sql_tuning_kit

Generate Oracle tuning scripts and explain-plan reports from SQL text and bind inputs.

## Installation

```bash
pip install oracle_sql_tuning_kit
```

## Quick Start

```python
from oracle_sql_tuning_kit import OracleSqlTuningKit

instance = OracleSqlTuningKit()
result = instance.run()
print(result)
```

## Features

- Template-based SQL*Plus scripts for plan, stats, and index checks
- Auto-parsed bind variable summary and recommended test harness
- One-command HTML/Markdown tuning report generation

## API Reference

### `OracleSqlTuningKit`

#### Constructor

```python
OracleSqlTuningKit(options: OracleSqlTuningKitOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `OracleSqlTuningKitResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/oracle_sql_tuning_kit/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
