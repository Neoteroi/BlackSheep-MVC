"""
Use this module to register required services.
Services registered inside a `rodi.Container` are automatically injected into request
handlers.

For more information and documentation, see `rodi` Wiki and examples:
    https://github.com/Neoteroi/rodi/wiki
    https://github.com/Neoteroi/rodi/tree/main/examples
"""
from typing import Tuple

from rodi import Container

from app.settings import Settings


def configure_services(
    settings: Settings,
) -> Tuple[Container, Settings]:
    container = Container()

    container.add_instance(settings)

    return container, settings
