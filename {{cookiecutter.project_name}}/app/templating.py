import os
from datetime import datetime

from blacksheep.server import Application
from blacksheep.server.rendering.jinja2 import JinjaRenderer
from blacksheep.settings.html import html_settings
from blacksheep.utils import join_fragments

from app.settings import Settings


def configure_templating(app: Application, settings: Settings) -> None:
    """
    Configures server side rendering for HTML views.
    """
    renderer = html_settings.renderer
    assert isinstance(renderer, JinjaRenderer)

    def get_copy():
        now = datetime.now()
        return "{} {}".format(now.year, settings.site.copyright)

    def get_bg_color():
        return os.environ.get("BG_COLOR", "#1abc9c")

    def abs_url(value: str = ""):
        prefix = app.router.prefix
        if not value and prefix and not prefix.endswith("/"):
            return prefix + "/"
        return join_fragments(prefix, value)

    helpers = {"bgcolor": get_bg_color, "copy": get_copy, "absurl": abs_url}

    renderer.env.globals.update(helpers)
