from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'ecommerce/home.html')

def index(request):
    return render(request,'ecommerce/index.html')

def gallery(request):
    return render(request,'ecommerce/gallery.html')

def faq(request):
    return render(request,'ecommerce/faq.html')

def contacts(request):
    return render(request,'ecommerce/contacts.html')

def checkout(request):
    return render(request,'ecommerce/checkout.html')

def catalog(request):
    return render(request,'ecommerce/catalog.html')

def catalog_product(request):
    return render(request,'ecommerce/catalog-product.html')

def cart(request):
    return render(request,'ecommerce/cart.html')

