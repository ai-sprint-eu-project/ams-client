# coding: utf-8

from .execution_time import (  # noqa: F401
    report_execution_time_metrics as report_execution_time
)
from .metric import report as report_metric  # noqa: F401
from .logging import initialise as initialise_logging  # noqa: F401
from .logging import tear_down as tear_down_logging  # noqa: F401


__version__ = '1.0'

__all__ = ['report_execution_time', 'report_metric',
           'initialise_logging', 'tear_down_logging']
