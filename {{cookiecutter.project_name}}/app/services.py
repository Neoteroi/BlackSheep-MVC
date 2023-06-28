"""
Use this module to register required services.
Services registered inside a `rodi.Container` are automatically injected into request
handlers.

For more information and documentation, see `rodi` Wiki and examples:
    https://github.com/Neoteroi/rodi/wiki
    https://github.com/Neoteroi/rodi/tree/main/examples
"""
from typing import Tuple

from config.common import Configuration
from rodi import Container


def configure_services(
    configuration: Configuration,
) -> Tuple[Container, Configuration]:
    container = Container()

    container.add_instance(configuration)

    return container, configuration
