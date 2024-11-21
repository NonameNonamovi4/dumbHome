from django.urls import path
from . import views
from .views import devices_home, toggle_device

urlpatterns = [
    path('devices/', devices_home, name='devices'),
    path('toggle/', toggle_device, name='toggle_device'),
]
