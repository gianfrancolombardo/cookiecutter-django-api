"""Post serializers."""

# Django Rest Framework
from rest_framework import serializers

# Models
from {{cookiecutter.project_slug}}.api.models import Post

class PostModelSerializer(serializers.ModelSerializer):
    """ Post model serializer

    Handle data validation and CRUD actions """

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'created'
        )

       