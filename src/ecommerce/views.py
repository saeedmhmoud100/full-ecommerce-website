from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views.generic import View,ListView
from .models import Product,ProductImg,ProductProperty,productComment,Cart
from .forms import ProductComment
# Create your views here.

def home(request):
    return render(request,'ecommerce/home.html')

def index(request):
    return render(request,'ecommerce/index.html')

class CatalogView(ListView):
    model = Product
    template_name = 'ecommerce/catalog.html'
    context_object_name = 'products'
    paginate_by = 6
    
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

class ProductFilterView(ListView):
    def get(self, request, *args, **kwargs):
        types = request.GET.getlist('type[]')
        screens = request.GET.getlist('screen[]')
        scr = request.GET.getlist('scrManufacturereen[]')
        tags = request.GET.get('tags' or None)
        price = request.GET.get('price')
        listby = request.GET.get('listby')
        allproducts = Product.objects.all()
        if listby:
            allproducts = allproducts.order_by(listby).distinct()
        if len(types)>0:
            allproducts = allproducts.filter(prodtype__in=types).distinct()
        if len(screens)>0:
            allproducts = allproducts.filter(screen_size__in=screens).distinct()
        if len(scr)>0:
            allproducts = allproducts.filter(Brand__in=scr).distinct()
        if tags:
            allproducts = allproducts.filter(tag1=tags)
        if price:
            allproducts = allproducts.filter(selling_price__lte=price)
        
        paginator = Paginator(allproducts, 6)

        page_number = request.GET.get('pag')
        page_obj = paginator.get_page(page_number)
        context = {
        'products':allproducts,
        'page_obj':page_obj
        }
        t = render_to_string('ecommerce/products.html',context)
        data = {
            'data':t,
            
        }
        return JsonResponse(data)

class CatalogProductView(View):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        images = ProductImg.objects.filter(product=pk)
        props = ProductProperty.objects.filter(product=pk)
        comments = productComment.objects.filter(product=pk)
        recom = Product.objects.all().order_by('-id')[:4]
        cou = images.count() + 1
        form = ProductComment()
        context = {
            'product':product,
            'images':images,
            'props':props,
            'comments':comments,
            'recom':recom,
            'cou':cou,
            'form':form
        }
        return render(request,'ecommerce/catalog-product.html',context)
    def post(self,request,pk):
        product = Product.objects.get(pk=pk)
        user = request.user
        form = ProductComment(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = user
            form_save.product = product
            form_save.save()
            messages.success(request,'added comment successfully!!')
            return redirect('catalog-product',pk=product.pk)

class CartView(View):
    def get(self,request):
        if request.user.is_authenticated:
            user = request.user
            carts = Cart.objects.filter(user=user)
            context = {
                'carts':carts
            }
        else:
            return redirect('login')
        return render(request,'ecommerce/cart.html',context)


def plus_or_minus_cart(request):
    state =request.GET.get('state')
    cart_id = request.GET.get('id')
    user = request.user
    cart = Cart.objects.get(pk=cart_id,user=user)
    if state == 'plus':
        cart.quantity += 1
        cart.save()
    if state == 'minus':
        if not cart.quantity == 1:
            cart.quantity -= 1
            cart.save()
    data = {
        'cart_quantity':cart.quantity,
        'cart_amount':cart.amount

    }
    return JsonResponse(data)

def remove_cart(request):
    cart_id = request.GET.get('id')
    Cart.objects.get(pk=cart_id,user=request.user).delete()
    data = {
        'yes':'yes'
    }
    return JsonResponse(data)
def gallery(request):
    return render(request,'ecommerce/gallery.html')

def faq(request):
    return render(request,'ecommerce/faq.html')

def contacts(request):
    return render(request,'ecommerce/contacts.html')

def checkout(request):
    return render(request,'ecommerce/checkout.html')


