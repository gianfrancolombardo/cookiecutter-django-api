# Django Api Cookiecutter

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter) and inspired by [Pydanny's cookiecutter](https://github.com/pydanny/cookiecutter-django) and [Cride-platzi](https://github.com/pablotrinidad/cride-platzi) and with the goal of optimize our development processes, we are happy to introduce our Django projects boilerplate packed and ready to use with the following features:

* **Python** 3.6
* **Django** 2.0.10
* **Django REST Framework** 3.9.1
* [**12 Factor**](https://12factor.net/) based settings
* **PostgreSQL** as database engine
* **Docker** as container engine
* Optimized development and production settings
* **User app** Comes with custom user app ready to go with [**JWT**](https://jwt.io/)
* **Extra** app for example
* Run tests with unittest or pytest
* **Flake8** for Style Guide Enforcement

## Installation

1. First, get [Cookiecutter](https://github.com/audreyr/cookiecutter). Trust me, it's awesome:

```
$ pip install cookiecutter
```

2. Run against this repo

```
$ cookiecutter https://github.com/gianfrancolombardo/cookiecutter-django-api
```

You'll be prompted for some values. Provide them, then a Django project will be created for you.

3. Enter the project and take a look around:

```
$ cd reddit/
$ ls
```
## Development

To start working on this project I highly recommend you to check
[pydanny's](https://github.com/pydanny) [Django Cookiecutter](https://github.com/pydanny/cookiecutter-django) [documentation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html) on how to get this project up and running locally. If you don't want to do so, just run:

```bash
$ docker-compose -f local.yml up --build
```

## Extra

This project provides a **simple application** that is responsible for the CRUD of a particular object (*Post* in this case). It also meets the REST API patterns.

Routes:
```
GET     /post       List
POST    /post       Create
GET     /post/123   Retrieve
PUT     /post/123   Update
DELETE  /post/123   Delete
PATCH   /post/123   Partial update
```

## Contributing

Please fill free to submit pull requests as well as open issues.