from datetime import datetime

from blacksheep.server import Application
from blacksheep.server.rendering.jinja2 import JinjaRenderer
from blacksheep.settings.html import html_settings
from config.common import Configuration


def configure_templating(
    application: Application, configuration: Configuration
) -> None:
    """
    Configures server side rendering for HTML views.
    """
    renderer = html_settings.renderer
    assert isinstance(renderer, JinjaRenderer)

    def get_copy():
        now = datetime.now()
        return "{} {}".format(now.year, configuration.site.copyright)

    helpers = {"_": lambda x: x, "copy": get_copy}

    env = renderer.env
    env.globals.update(helpers)
