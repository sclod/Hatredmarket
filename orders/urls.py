from django.urls import path
from .views import basket, delivery


urlpatterns = [
    path('basket', basket),
    path('delivery', delivery)
]
