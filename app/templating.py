from datetime import datetime

from blacksheep.server import Application
from blacksheep.server.templating import use_templates
from config.common import Configuration
from jinja2 import Environment, PackageLoader


def configure_templating(
    application: Application, configuration: Configuration
) -> None:
    """
    Configures server side templating engine for HTML views, using Jinja2.
    """
    use_templates(application, PackageLoader("app", "views"))

    def get_copy():
        now = datetime.now()
        return "{} {}".format(now.year, configuration.site.copyright)

    helpers = {"_": lambda x: x, "copy": get_copy}

    env: Environment = application.jinja_environment  # type: ignore
    env.globals.update(helpers)
