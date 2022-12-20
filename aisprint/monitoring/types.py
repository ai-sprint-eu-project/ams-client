# coding: utf-8

from sys import version_info
from typing import Union

from fluent.handler import FluentHandler  # type: ignore


Value = Union[int, float, str, bool]

if (
    (version_info.major > 3)
    or (version_info.major == 3 and version_info.minor >= 9)
):
    Tags = dict[str, str]  # type: ignore
    Values = Union[Value, dict[str, Value]]  # type: ignore
else:
    Tags = dict  # type: ignore
    Values = Union[Value, dict]  # type: ignore

LoggingContext = FluentHandler
