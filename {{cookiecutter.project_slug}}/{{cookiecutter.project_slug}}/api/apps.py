"""Api app."""

# Django
from django.apps import AppConfig

class ApiAppConfig(AppConfig):
    """api app config."""

    name = '{{cookiecutter.project_slug}}.api'
    verbose_name = 'Api'
