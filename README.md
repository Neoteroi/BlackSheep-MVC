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
In both cases, services configured at startup and described in handlers' signatures, are injected automatically by the framework (see app.services and how the `Container` class is used).
Controllers *also* receive injected services to their constructors (`__init__` methods), hence potentially reducing code repetition.

Controllers also offer extra extensibility points: `on_request`, `on_response`, base `route` for all handlers defined on the class, and automatic selection of `view` by method name.

```python
from blacksheep.server.controllers import Controller, get


class Home(Controller):
    @get()
    def index(self):
        # Since the @get() decorator is used without arguments, the URL path
        # is by default "/"

        # Since the view function is called without parameters, the name is
        # obtained from the calling request handler: 'index',
        # -> /views/home/index.html
        return self.view()

    @get(None)
    def example(self):
        # Since the @get() decorator is used explicitly with None, the URL path
        # is obtained from the method name: "/example"

        # Since the view function is called without parameters, the name is
        # obtained from the calling request handler: 'example',
        # -> /views/home/example.html
        return self.view()
```

It is also possible to define API endpoints:

```python
from blacksheep import Response
from blacksheep.server.controllers import ApiController, delete, get, patch, post


# In this case, the entity name is obtained from the class name: "cats"
# To specify a @classmethod called "class_name" and returning a string, like in the
# Foo example below.
class Cats(ApiController):
    @get(":cat_id")
    def get_cat(self, cat_id: str) -> Response:
        """
        Handles GET /api/cats/:id
        """

    @patch(":cat_id")
    def update_cat(self, cat_id: str) -> Response:
        """
        Handles PATCH /api/cats/:id
        """

    @post()
    def create_cat(self) -> Response:
        """
        Handles POST /api/cats
        """

    @delete(":cat_id")
    def delete_cat(self, cat_id: str) -> Response:
        """
        Handles DELETE /api/cats/:id
        """


class FooExample(ApiController):
    @classmethod
    def class_name(cls) -> str:
        return "foo"

    @get(":cat_id")
    def get_cat(self, cat_id: str) -> Response:
        """
        Handles GET /api/foo/:id
        """
```

---

## About dependency injection
For more information and documentation about built-in dependency injection, see `rodi` Wiki and examples:

* [rodi](https://github.com/RobertoPrevato/rodi)
* [rodi wiki](https://github.com/RobertoPrevato/rodi/wiki)
* [rodi wiki examples](https://github.com/RobertoPrevato/rodi/wiki/Examples)

---

## About ASGI servers
This project template includes references to [`uvicorn`](uvicorn.org).

To run with hot reload during local development and using a custom port:

```bash
uvicorn server:app --port 44777 --reload --log-level info
```

However, it is possible to use other implementations of ASGI HTTP Servers.
For example, to use the same application with [`Hypercorn`](https://pypi.org/project/Hypercorn/):

```bash
$ pip install Hypercorn

$ hypercorn server:app
```

## Developing locally using HTTPS
To develop locally over HTTPS using a trusted certificate, see
[_How to develop locally using HTTPS_](https://github.com/RobertoPrevato/BlackSheep/wiki/How-to-develop-locally-using-HTTPS).
