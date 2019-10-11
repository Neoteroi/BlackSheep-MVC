from rodi import Container
from roconfiguration import Configuration
from blacksheep.server import Application
from core.events import ServicesRegistrationContext
from .auth import configure_authentication
from .errors import configure_error_handlers
from .templating import configure_templating
# noinspection PyUnresolvedReferences
from .controllers import home


def configure_application(services: Container,
                          context: ServicesRegistrationContext,
                          configuration: Configuration):
    app = Application(services=services,
                      show_error_details=configuration.show_error_details,
                      debug=configuration.debug)

    app.on_start += context.initialize
    app.on_stop += context.dispose

    configure_error_handlers(app)
    configure_authentication(app)
    configure_templating(app, configuration)

    app.serve_files('app/static')

    return app
