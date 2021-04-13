from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product
from django.http import JsonResponse


def index(request):
    return render(request, 'catalog/index.html', context={
        'title': 'Одежда',
        'all_products': Product.objects.all(),
    })


def accessories(request):
    return render(request, 'catalog/accessories.html', context={
        'title': 'Аксессуары'
    })


def product(request, cid):
    return render(request, 'catalog/product.html', context={
        'title': 'Выборка по категории',
        'all_products': Product.objects.filter(category_id=cid),
    })


def ajax_select(request):
    cid = request.GET.get['cid']
    return JsonResponse({
        'all_products': Product.objects.filter(category_id=cid)
    })

