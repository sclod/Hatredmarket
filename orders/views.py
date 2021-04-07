from django.shortcuts import render


def basket(request):
    return render(request, 'orders/basket.html', context={
        'title': 'Корзина'
    })


def delivery(request):
    return render(request, 'orders/delivery.html', context={
        'title': 'Оформления заказа'
    })
