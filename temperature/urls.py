from django.urls import path
from . import views

urlpatterns = [
    path('temperature/', views.temperature_view, name='temperature_view'),
]