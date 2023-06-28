"""
This module configures the BlackSheep application before it starts.
"""
from blacksheep import Application
from rodi import Container

from app.auth import configure_authentication
{%- if cookiecutter.use_openapi == "True" %}
from app.docs import configure_docs
{%- endif %}
from app.errors import configure_error_handlers
from app.services import configure_services
from app.settings import load_settings, Settings
from app.templating import configure_templating


def configure_application(
    services: Container,
    settings: Settings,
) -> Application:
    app = Application(
        services=services, show_error_details=settings.app.show_error_details
    )

    app.serve_files("app/static")
    configure_error_handlers(app)
    configure_authentication(app, settings)
{%- if cookiecutter.use_openapi == "True" %}
    configure_docs(app, settings)
{%- endif %}
    configure_templating(app, settings)
    return app


app = configure_application(*configure_services(load_settings()))
