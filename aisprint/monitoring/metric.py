# coding: utf-8

from typing import Optional

from ._utils import get_telegraf_client
from .types import Values, Tags


def report(
    name: str,
    values: Values,
    tags: Optional[Tags] = None
) -> None:
    telegraf_client = get_telegraf_client(tags)
    telegraf_client.metric(name, values)
