{%- if cookiecutter.app_settings_library == "Pydantic" -%}
"""
Application settings handled using Pydantic Settings management

https://docs.pydantic.dev/latest/usage/settings/
"""
from pydantic import BaseModel, BaseSettings


class APIInfo(BaseModel):
    title = "{{ cookiecutter.project_name }} API"
    version = "0.0.1"


class App(BaseModel):
    show_error_details = False


class Site(BaseModel):
    copyright: str = "Example"


class Settings(BaseSettings):
    # to override info:
    # export app_info='{"title": "x", "version": "0.0.2"}'
    info: APIInfo = APIInfo()

    # to override app:
    # export app_app='{"show_error_details": True}'
    app: App = App()

    site: Site = Site()

    class Config:
        env_prefix = "APP_"  # defaults to no prefix, i.e. ""


def load_settings() -> Settings:
    return Settings()

{%- else -%}
"""
Application settings handled using essentials-configuration.

https://github.com/Neoteroi/essentials-configuration
"""
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


Settings = Configuration


def load_settings() -> Settings:
    return default_configuration()
{%- endif %}
