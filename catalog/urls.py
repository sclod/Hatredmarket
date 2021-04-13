from django.urls import path, re_path
from .views import index, accessories, product


urlpatterns = [
    path('index', index),
    path('accessories', accessories),
    path('product', product)
]
