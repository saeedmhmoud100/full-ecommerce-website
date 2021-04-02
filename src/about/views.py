from django.shortcuts import render

# Create your views here.


def faq(request):
    return render(request,'ecommerce/faq.html')

def contacts(request):
    return render(request,'ecommerce/contacts.html')


