# BlackSheep-MVC Cookiecutter template
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to
boostrap a new BlackSheep v2 application to build a Web API.

## Getting started

```bash
pip install blacksheep-cli
```

```bash
blacksheep create --template mvc

🚀 Project name example
📜 Use OpenAPI Documentation? Yes
🔧 Library to read settings Pydantic
```

## Documentation
The documentation of the [framework can be read here](https://www.neoteroi.dev/blacksheep/).

## Features

- Basic folder structure
- Settings handled using [Pydantic Settings Management](https://docs.pydantic.dev/latest/usage/settings/) or [essentials-configuration](https://github.com/Neoteroi/essentials-configuration)
  to read combined with Pydantic for validation
- Strategy to read configuration from YAML, TOML, JSON, INI files, and
  environmental variables, or settings stored in a user's folder using
  [`essentials-configuration`](https://github.com/Neoteroi/essentials-configuration)
- Handling of [dependency injection](https://www.neoteroi.dev/blacksheep/dependency-injection/), using [`rodi`](https://github.com/RobertoPrevato/rodi)
- Configuration of exceptions handlers
- Strategy to handle [authentication](https://www.neoteroi.dev/blacksheep/authentication/) and [authorization](https://www.neoteroi.dev/blacksheep/authorization/), using [`guardpost`](https://github.com/RobertoPrevato/GuardPost)

## For more information on rodi

For more information and documentation about `rodi`, see:

- [dependency injection in BlackSheep](https://www.neoteroi.dev/blacksheep/dependency-injection/)
- [rodi](https://github.com/RobertoPrevato/rodi)

## Using Cookiecutter
The template can also be used with `Cookiecutter`.

```bash
pip install cookiecutter

cookiecutter https://github.com/Neoteroi/BlackSheep-MVC
```
