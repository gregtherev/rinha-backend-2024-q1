from django.contrib import admin
from django.urls import path
from .api import api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_router.urls)
]
