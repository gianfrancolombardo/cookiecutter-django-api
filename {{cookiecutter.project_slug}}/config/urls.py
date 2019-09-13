"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('api/', include(('{{cookiecutter.project_slug}}.api.urls', 'api'), namespace='apis')),
    path('', include(('{{cookiecutter.project_slug}}.users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
