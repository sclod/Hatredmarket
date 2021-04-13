from django.urls import path
from .views import index, contacts, newslatter


urlpatterns = [
    path('', index),
    path('index', index),
    path('contacts', contacts),
    path('newslatter', newslatter)
]
