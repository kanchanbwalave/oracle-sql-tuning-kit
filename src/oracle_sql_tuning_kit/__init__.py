"""
oracle_sql_tuning_kit - Generate Oracle tuning scripts and explain-plan reports from SQL text and bind inputs.
"""

__version__ = "0.1.0"

from .templatebased_sqlplus_scripts_ import OracleSqlTuningKit
from .types import OracleSqlTuningKitOptions, OracleSqlTuningKitResult
from .exceptions import OracleSqlTuningKitError, ConfigurationError, ValidationError

__all__ = [
    "OracleSqlTuningKit",
    "OracleSqlTuningKitOptions",
    "OracleSqlTuningKitResult",
    "OracleSqlTuningKitError",
    "ConfigurationError",
    "ValidationError",
]
