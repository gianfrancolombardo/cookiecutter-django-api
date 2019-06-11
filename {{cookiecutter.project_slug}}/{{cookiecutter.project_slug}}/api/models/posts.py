"""Post model."""

# Django
from django.db import models

#Own
from {{cookiecutter.project_slug}}.utils.models import BaseModel

class Post(BaseModel):
    """ Post model

    A simple example of a Post model """

    title = models.CharField(
        max_length=100,
        help_text="Title of the post"
    )
    body = models.TextField(
        help_text="Body of the post"
    )
   
    def __str__(self):
        """Return post title."""
        return self.title

    class Meta:
        """Meta class."""

        ordering = ['-created', '-modified']

       