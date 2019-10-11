from datetime import datetime
from roconfiguration import Configuration
from blacksheep.server import Application
from blacksheep.server.templating import use_templates, PackageLoader, Environment


def configure_templating(application: Application, configuration: Configuration):
    use_templates(application, PackageLoader(__name__, 'views'))

    def get_copy():
        now = datetime.now()
        return "{} {}".format(now.year, configuration.site.copyright)

    helpers = {
        '_': lambda x: x,
        'copy': get_copy
    }

    # noinspection PyUnresolvedReferences
    env = application.jinja_environment  # type: Environment
    env.globals.update(helpers)
