#!/usr/bin/env python3
"""Basic usage example for oracle_sql_tuning_kit."""

from oracle_sql_tuning_kit import OracleSqlTuningKit, OracleSqlTuningKitOptions


def main() -> None:
    # Create with default options
    instance = OracleSqlTuningKit()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = OracleSqlTuningKitOptions(verbose=True)
    instance = OracleSqlTuningKit(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
