"""Type definitions for oracle_sql_tuning_kit."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class OracleSqlTuningKitOptions:
    """Configuration options for OracleSqlTuningKit.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Template-based SQL*Plus scripts for plan, stats, and index checks
        feature_2: Configuration for: Auto-parsed bind variable summary and recommended test harness
        feature_3: Configuration for: One-command HTML/Markdown tuning report generation
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None


@dataclass
class OracleSqlTuningKitResult:
    """Result returned by OracleSqlTuningKit operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
