from blacksheep.server.env import get_env, is_development
from config.common import Configuration, ConfigurationBuilder
from config.env import EnvVars
from config.user import UserSettings
{%- if cookiecutter.app_settings_format == "INI" %}
from config.ini import INIFile
{%- endif %}
{%- if cookiecutter.app_settings_format == "JSON" %}
from config.json import JSONFile
{%- endif %}
{%- if cookiecutter.app_settings_format == "YAML" %}
from config.yaml import YAMLFile
{%- endif %}
{%- if cookiecutter.app_settings_format == "TOML" %}
from config.toml import TOMLFile
{%- endif %}


def default_configuration_builder() -> ConfigurationBuilder:
    app_env = get_env()
    builder = ConfigurationBuilder(
{%- if cookiecutter.app_settings_format == "INI" %}
        INIFile(f"settings.ini"),
        INIFile(f"settings.{app_env.lower()}.ini", optional=True),
{%- endif %}
{%- if cookiecutter.app_settings_format == "JSON" %}
        JSONFile(f"settings.json"),
        JSONFile(f"settings.{app_env.lower()}.json", optional=True),
{%- endif %}
{%- if cookiecutter.app_settings_format == "YAML" %}
        YAMLFile(f"settings.yaml"),
        YAMLFile(f"settings.{app_env.lower()}.yaml", optional=True),
{%- endif %}
{%- if cookiecutter.app_settings_format == "TOML" %}
        TOMLFile(f"settings.toml"),
        TOMLFile(f"settings.{app_env.lower()}.toml", optional=True),
{%- endif %}
        EnvVars("APP_"),
    )

    if is_development():
        # for development environment, settings stored in the user folder
        builder.add_source(UserSettings())

    return builder


def default_configuration() -> Configuration:
    builder = default_configuration_builder()

    return builder.build()


def load_configuration() -> Configuration:
    return default_configuration()
