from django import contrib
from django.contrib import admin
from django.urls import include, path

from monetarium.settings import ADMIN_ENABLED

urlpatterns = [
        path("", include("apps.core.urls")),
        path("api/", include("apps.api.urls"))
    ]

if ADMIN_ENABLED:
    urlpatterns += [
            path('admin/', admin.site.urls),
        ]
