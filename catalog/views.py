from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product


def index(request):
    category = None
    product = Product.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'catalog/index.html', context={
        'title': 'Одежда',
        'category': category,
        'categories': categories,
        'products': products,
        'all_products': product
    })


def accessories(request):
    return render(request, 'catalog/accessories.html', context={
        'title': 'Аксессуары'
    })


def product(request, cid):
    return render(request, 'catalog/product.html', context={
        'title': 'Выборка по категории',
        'sel_goods': Product.objects.filter(category_id=cid)
    })

