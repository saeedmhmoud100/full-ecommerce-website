from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from.models import Product
# Create your views here.

def home(request):
    return render(request,'ecommerce/home.html')

def index(request):
    return render(request,'ecommerce/index.html')


class CatalogView(View):
    def get(self,request):
        products = Product.objects.all()
        context = {
            'products':products
        }
        return render(request,'ecommerce/catalog.html',context)

class CatalogProductView(View):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        return render(request,'ecommerce/catalog-product.html')

# def catalog_product(request):
#     return render(request,'ecommerce/catalog-product.html')


def gallery(request):
    return render(request,'ecommerce/gallery.html')

def faq(request):
    return render(request,'ecommerce/faq.html')

def contacts(request):
    return render(request,'ecommerce/contacts.html')

def checkout(request):
    return render(request,'ecommerce/checkout.html')


def cart(request):
    return render(request,'ecommerce/cart.html')

