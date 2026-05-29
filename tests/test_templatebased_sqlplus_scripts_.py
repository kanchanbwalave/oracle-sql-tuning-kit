"""Tests for oracle_sql_tuning_kit."""

from oracle_sql_tuning_kit import OracleSqlTuningKit, OracleSqlTuningKitOptions


class TestOracleSqlTuningKit:
    def test_create_instance_with_defaults(self) -> None:
        instance = OracleSqlTuningKit()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = OracleSqlTuningKitOptions(verbose=True)
        instance = OracleSqlTuningKit(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = OracleSqlTuningKit()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = OracleSqlTuningKit()
        result = instance.run()
        assert result.error is None
