# {{ cookiecutter.project_name }}

Project template for [BlackSheep](https://github.com/Neoteroi/BlackSheep)
web framework to start Web APIs.

## Getting started

1. create a Python virtual environment
2. install dependencies
3. run the application

### For Linux and Mac

```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python dev.py
```

### For Windows

```bash
py -3.13 -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python dev.py
```

### Env variables

To test applying a different color to the top section, set an env variable
`BG_COLOR` with a valid value for a CSS color.

```bash
BG_COLOR="#fd7e14" python dev.py
```

To test serving the application at a different path prefix, set an env variable
`APP_ROUTE_PREFIX` with the desired prefix. This feature is available since
BlackSheep 2.1.0, and can be useful when using a proxy server and path based
routing.

```bash
APP_ROUTE_PREFIX="orange" python dev.py
```

### Docker

Build an image using the example image.

```bash
docker build -t mvcdemo .
```

Run the image once built, for example to map from the host `8080`:

```bash
docker run --rm -p 8080:80 mvcdemo
```

To test running with customizations to test the application at a different
path:

```bash
docker run --name mvcdemo --rm -p 8080:80 -e BG_COLOR='#fd7e14' -e APP_ROUTE_PREFIX='orange' mvcdemo
```

Then navigate to [http://localhost:8080/orange/](http://localhost:8080/orange/).
