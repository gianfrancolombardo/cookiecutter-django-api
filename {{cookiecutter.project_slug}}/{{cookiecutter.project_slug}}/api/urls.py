"""api URLs."""

# Django
from django.urls import include, path



# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from {{cookiecutter.project_slug}}.api.views import posts as post_views

router = DefaultRouter()
router.register(r'posts', post_views.PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls))
]
