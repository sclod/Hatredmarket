from django.shortcuts import render
from catalog.models import Product


def index(request):
    product = Product.objects.all()
    return render(request, 'home/index.html', context={
        'title': 'Одежда',
        'all_products': product
    })


def contacts(request):
    return render(request, 'home/contacts.html', context={
        'title': 'Контакты'
    })


