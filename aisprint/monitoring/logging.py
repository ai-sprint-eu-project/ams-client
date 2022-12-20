# coding: utf-8

import logging
from logging import Logger
from typing import Callable, Optional, Union

from fluent.handler import FluentRecordFormatter  # type: ignore

from ._constants import FLUENT_DEFAULT_FORMAT
from ._utils import get_fluent_handler
from .types import LoggingContext


def initialise(name: Optional[str] = None, host: Optional[str] = None,
               port: Optional[int] = None,
               fmt: Union[None, dict, Callable] = None,
               root_logger: Optional[Logger] = None) -> LoggingContext:
    if root_logger is None:
        root_logger = logging.getLogger()
    fluent_handler = get_fluent_handler(name, host, port)
    if fmt is None:
        fmt = FLUENT_DEFAULT_FORMAT
    formatter = FluentRecordFormatter(fmt)
    fluent_handler.setFormatter(formatter)
    root_logger.addHandler(fluent_handler)
    return fluent_handler


def tear_down(ctx: LoggingContext) -> None:
    ctx.close()
