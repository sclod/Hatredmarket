from django.shortcuts import render
from django.core.mail import send_mail
from catalog.models import Product
from .models import Feedback, UserEmail


def index(request):
    product = Product.objects.all()
    return render(request, 'home/index.html', context={
        'title': 'Главная',
        'all_products': product,
    })


def contacts(request):
    if request.method == 'GET':
        return render(request, 'home/contacts.html', context={})
    if request.method == 'POST':
        feedback = Feedback()
        feedback.subject = request.POST.get('subject')
        feedback.message = request.POST.get('message')
        feedback.user_email = request.POST.get('email')
        feedback.save()

        site_response = """
        Your letter is in progress ...    
        """
        result = send_mail(feedback.subject, site_response, 'My company',
                           [feedback.user_email], fail_silently=False)
        if result == 0:
            return render(request, 'home/index.html')
        elif result == 1:
            return render(request, 'home/contacts.html')


def newslatter(request):
    if request.method == 'GET':
        return render(request, 'home/index.html', context={})
    if request.method == 'POST':
        reg_email = request.POST.get('email')
        body = """
        Hello, esteemed user!
        You have subscribed to the newsletter from [My Site].
        We are open 24/7!
        You can contact our support team 24/7

        We will be glad to be of service to you!
        Come back more often!
        """
        user_email = UserEmail(email=reg_email)
        user_email.save()
        result = send_mail('Subscribe', body, 'My company', [reg_email], fail_silently=False)
        if result == 0:
            return render(request, 'home/contacts.html')
        elif result == 1:
            return render(request, 'home/index.html')
