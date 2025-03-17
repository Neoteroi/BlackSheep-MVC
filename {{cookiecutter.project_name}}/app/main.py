"""
This module configures the BlackSheep application before it starts.
"""
from blacksheep import Application
from rodi import Container

from app.auth import configure_authentication
from app.diagnostics import get_diagnostic_app
{%- if cookiecutter.use_openapi %}
from app.docs import configure_docs
{%- endif %}
from app.errors import configure_error_handlers
from app.services import configure_services
from app.settings import Settings
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
{%- if cookiecutter.use_openapi %}
    configure_docs(app, settings)
{%- endif %}
    configure_templating(app, settings)
    return app


def get_app():
    try:
        return configure_application(*configure_services())
    except Exception as exc:
        return get_diagnostic_app(exc)


app = get_app()
