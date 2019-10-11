"""
Use this module to register required services.
Services registered inside a `rodi.Container` are automatically injected into request handlers.

For more information and documentation, see `rodi` Wiki and examples:
    https://github.com/RobertoPrevato/rodi/wiki
    https://github.com/RobertoPrevato/rodi/wiki/Examples
"""
from rodi import Container
from roconfiguration import Configuration
from core.events import ServicesRegistrationContext
from typing import Tuple


def configure_services(configuration: Configuration) \
        -> Tuple[Container, ServicesRegistrationContext, Configuration]:
    container = Container()

    context = ServicesRegistrationContext()

    container.add_instance(configuration)

    return container, context, configuration
