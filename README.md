# BlackSheep MVC project template
Project template for [BlackSheep](https://github.com/RobertoPrevato/BlackSheep) web applications using MVC architecture. This project template
can be used to build web applications that serve static files, support server side rendering of HTML, and define APIs.

[![Picture](https://labeuwstacc.blob.core.windows.net/posts/blacksheep-mvc.png)](#blacksheep-mvc-project-template)

## Getting started
1. Clone the repository

```bash
$ git clone https://github.com/RobertoPrevato/BlackSheepMVC.git yourproject
```

2. Navigate to its folder

3. Create a Python virtual environment and install requirements.txt

4. Run the application
```bash
$ uvicorn server:app --port 44777 --reload --log-level info
```

## Features
* Basic folder structure
* Strategy to organize request handlers in controllers, and folder structure of views (HTML templates used by Jinja2)
* Strategy to read configuration from YAML, JSON, INI files, and environmental variables; using [`roconfiguration`](https://github.com/RobertoPrevato/roconfiguration)
* Handling of dependency injection, using [`rodi`](https://github.com/RobertoPrevato/rodi) :tulip:
* Configuration of exceptions handlers
* Handling of application start and stop events
* Strategy to handle authentication and authorization, using [`guardpost`](https://github.com/RobertoPrevato/GuardPost)
* Integration with [`Jinja2 template engine`](http://jinja.pocoo.org/docs/2.10/)

## Request handlers defined using Controllers
In BlackSheep, request handlers can be defined as functions, or class methods.
Using class methods has the benefit of reducing code repetition, when the same context is needed for several request handlers.
In both cases, services configured at startup (see app.services and how the `Container` class is used) and described in handlers' signatures, are injected automatically by the framework.
Controllers *also* receive injected services to their constructors (`__init__` methods).

Controllers also offer extra extensibility points: `on_request`, `on_response`, base `route` for all handlers defined on the class, and automatic selection of `view` by method name.

```python
from blacksheep.server.controllers import Controller, get


class Home(Controller):

    @get()
    def index(self):
        # NB: since the view function is called without parameters, the name is obtained from the
        # calling request handler ('index')
        return self.view()  # <-- returns by default /views/home/index.html

    @get(...)  # <-- Since ellipsis is used here, the route takes the name of the request handler: '/about'
    def about(self):
        return self.view()  # <-- returns by default /views/home/about.html
```

---

## About dependency injection
For more information and documentation about built-in dependency injection, see `rodi` Wiki and examples:

* [rodi](https://github.com/RobertoPrevato/rodi)
* [rodi wiki](https://github.com/RobertoPrevato/rodi/wiki)
* [rodi wiki examples](https://github.com/RobertoPrevato/rodi/wiki/Examples)

---

## About ASGI servers
This project template includes references to [`uvicorn`](uvicorn.org). However, it is possible to use other implementations of ASGI HTTP Servers.

For example, to use the same application with [`Hypercorn`](https://pypi.org/project/Hypercorn/):

```bash
$ pip install Hypercorn

$ hypercorn server:app
```
