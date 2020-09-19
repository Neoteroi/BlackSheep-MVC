from roconfiguration import Configuration
from rodi import Container

from blacksheep.server import Application
from blacksheep.server.files import ServeFilesOptions
from core.events import ServicesRegistrationContext

from . import controllers  # NoQA
from .auth import configure_authentication
from .errors import configure_error_handlers
from .templating import configure_templating


def configure_application(
    services: Container,
    context: ServicesRegistrationContext,
    configuration: Configuration,
) -> Application:
    app = Application(
        services=services,
        show_error_details=configuration.show_error_details,
        debug=configuration.debug,
    )

    app.on_start += context.initialize
    app.on_stop += context.dispose

    configure_error_handlers(app)
    configure_authentication(app)
    configure_templating(app, configuration)

    app.serve_files(ServeFilesOptions("app/static"))
    return app
