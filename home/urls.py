from django.urls import path
from .views import index, contacts


urlpatterns = [
    path('', index),
    path('index', index),
    path('contacts', contacts)
]
