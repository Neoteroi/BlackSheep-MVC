import os
import shutil


project_name = "{{ cookiecutter.project_name }}"
settings_library = "{{ cookiecutter.app_settings_library }}"
settings_format = "{{ cookiecutter.app_settings_format }}"
use_openapi = "{{ cookiecutter.use_openapi }}" == "True"

remove_paths = []

if not use_openapi:
    remove_paths.append("app/docs")

for possible_format in {"toml", "yaml", "ini", "json"}:
    if (
        settings_library != "essentials-configuration"
        or settings_format.lower() != possible_format
    ):
        remove_paths.append(f"settings.{possible_format}")
        remove_paths.append(f"settings.dev.{possible_format}")


def remove(item_path: str):
    item_path = item_path.strip()
    if item_path and os.path.exists(item_path):
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.unlink(item_path)


for path in remove_paths:
    remove(path)
