# coding: utf-8

from os import environ
from typing import Optional

from telegraf.client import TelegrafClient  # type: ignore
from fluent.handler import FluentHandler  # type: ignore

from ._constants import (TELEGRAF_HOST_VARIABLE_NAME, TELEGRAF_DEFAULT_HOST,
                         TELEGRAF_PORT_VARIABLE_NAME, TELEGRAF_DEFAULT_PORT,
                         COMPONENT_NAME_VARIABLE_NAME,
                         FLUENT_HOST_VARIABLE_NAME, FLUENT_DEFAULT_HOST,
                         FLUENT_PORT_VARIABLE_NAME, FLUENT_DEFAULT_PORT)
from .types import Tags


def _get_port(svc_name: str, var_name: str, var_default: int) -> int:
    port = environ.get(var_name, var_default)
    try:
        return int(port)
    except ValueError as e:
        raise RuntimeError(
            f'erroneous {svc_name} port number: "{port}"'
        ) from e


def get_telegraf_client(
    tags: Optional[Tags] = None
) -> TelegrafClient:
    host = environ.get(TELEGRAF_HOST_VARIABLE_NAME, TELEGRAF_DEFAULT_HOST)
    port = _get_port('Telegraf', TELEGRAF_PORT_VARIABLE_NAME,
                     TELEGRAF_DEFAULT_PORT)
    return TelegrafClient(host=host, port=port, tags=tags)


def get_fluent_handler(name: Optional[str], host: Optional[str],
                       port: Optional[int]) -> FluentHandler:
    if name is None:
        name = environ.get(COMPONENT_NAME_VARIABLE_NAME)
        if name is None:
            raise RuntimeError(f'no component name'
                               f' (is environment variable '
                               f'"{COMPONENT_NAME_VARIABLE_NAME}" set?)')
    if host is None:
        host = environ.get(FLUENT_HOST_VARIABLE_NAME, FLUENT_DEFAULT_HOST)
    if port is None:
        port = _get_port('Fluent', FLUENT_PORT_VARIABLE_NAME,
                         FLUENT_DEFAULT_PORT)
    return FluentHandler(name, host, port)
