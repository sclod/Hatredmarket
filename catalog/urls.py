from django.conf.urls import url
from django.urls import path
from . import views
from .views import index, accessories, product


urlpatterns = [
    path('index', index),
    path('accessories', accessories),
    path('product', product),
]
