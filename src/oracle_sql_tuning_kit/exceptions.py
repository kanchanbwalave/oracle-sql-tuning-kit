"""Custom exceptions for oracle_sql_tuning_kit."""

from __future__ import annotations


class OracleSqlTuningKitError(Exception):
    """Base exception for all OracleSqlTuningKit errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(OracleSqlTuningKitError):
    """Raised when the SDK is misconfigured."""


class ValidationError(OracleSqlTuningKitError):
    """Raised when input validation fails."""


class TimeoutError(OracleSqlTuningKitError):
    """Raised when an operation exceeds its time limit."""
