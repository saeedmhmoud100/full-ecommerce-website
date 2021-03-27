from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
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


def favorite_or_unfavorite(request):
    id = request.GET.get('id',None)
    user = request.user
    product = Product.objects.get(id=id)
    
    if user in product.favourites.all():
        product.favourites.remove(user)
    else:
        product.favourites.add(user)
    data={
        'id':id
    }
    return JsonResponse(data)

def product_type_filter(request):
    types = request.GET.getlist('type[]')
    screens = request.GET.getlist('screen[]')
    scr = request.GET.getlist('scrManufacturereen[]')
    allproducts = Product.objects.all().order_by('-id')
    if len(types)>0:
        allproducts = allproducts.filter(prodtype__in=types).distinct()
    if len(screens)>0:
        allproducts = allproducts.filter(screen_size__in=screens).distinct()
    if len(scr)>0:
        allproducts = allproducts.filter(Brand__in=scr).distinct()

    context={
        'products':allproducts,
    }
    t = render_to_string('ecommerce/products.html',context)
    data = {
        'data':t
    }
    return JsonResponse(data)

class CatalogProductView(View):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        return render(request,'ecommerce/catalog-product.html')

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

