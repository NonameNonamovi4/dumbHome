from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alerts.urls')),
    path('', include('devices.urls')),
    path('', include('cameras.urls')),
    path('', include('home.urls')),
    path('', include('temperature.urls'))
]