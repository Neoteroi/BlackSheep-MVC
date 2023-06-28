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
🔧 App settings format (Use arrow keys)
 » YAML
   TOML
   JSON
   INI
```

## Documentation
The documentation of the [framework can be read here](https://www.neoteroi.dev/blacksheep/).

## Features

- Basic folder structure
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
- [rodi wiki](https://github.com/RobertoPrevato/rodi/wiki)
- [rodi wiki examples](https://github.com/RobertoPrevato/rodi/wiki/Examples)

## Using Cookiecutter
The template can also be used with `Cookiecutter`.

```bash
pip install cookiecutter

cookiecutter https://github.com/Neoteroi/BlackSheep-MVC
```
