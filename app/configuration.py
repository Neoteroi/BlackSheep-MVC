from config.common import Configuration, ConfigurationBuilder
from config.env import EnvVars
from config.yaml import YAMLFile


def load_configuration() -> Configuration:
    builder = ConfigurationBuilder(
        YAMLFile("settings.yaml"),
        EnvVars()
    )
    return builder.build()
