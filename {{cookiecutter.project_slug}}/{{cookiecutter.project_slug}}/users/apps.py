"""Users app."""

# Django
from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """Users app config."""

    name = '{{cookiecutter.project_slug}}.users'
    verbose_name = 'Users'
