from django.urls import path
from . import views

urlpatterns = [
    path('live/', views.livefe, name='live_feed'),  # URL for the video stream
    path('cameras/', views.video_page, name='cameras'),  # URL for the HTML page
]