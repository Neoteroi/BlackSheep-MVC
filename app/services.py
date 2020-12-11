"""
Use this module to register required services.
Services registered inside a `rodi.Container` are automatically injected into request
handlers.

For more information and documentation, see:
    https://www.neoteroi.dev/blacksheep/dependency-injection/
"""
from typing import Tuple

from roconfiguration import Configuration
from rodi import Container

from core.events import ServicesRegistrationContext


def configure_services(
    configuration: Configuration,
) -> Tuple[Container, ServicesRegistrationContext, Configuration]:
    container = Container()

    context = ServicesRegistrationContext()

    container.add_instance(configuration)

    # Use the container object for example to register dependent services such as
    # classes used to connect to a database or other services, or to handle business
    # logic. Services registered here automatically injected into request handlers
    # when their function signature is type annotated with matching types.

    return container, context, configuration
