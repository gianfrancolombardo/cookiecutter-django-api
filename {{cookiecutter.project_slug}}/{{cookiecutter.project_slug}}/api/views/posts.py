"""Post views."""

# Django Rest Framework
from rest_framework import viewsets

# Own
from {{cookiecutter.project_slug}}.api.serializers import PostModelSerializer
from {{cookiecutter.project_slug}}.api.models import Post

class PostViewSet(viewsets.ModelViewSet):
    """ Post view set
        Handle all CRUD requests
    """

    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    
       