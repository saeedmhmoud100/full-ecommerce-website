from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('faq/',views.faq,name='faq'),
    path('contacts/',views.contacts,name='contacts'),
    path('checkout/',views.checkout,name='checkout'),
    path('catalog/',views.catalog,name='catalog'),
    path('catalogproduct/',views.catalog_product,name='catalog-product'),
    path('cart/',views.cart,name='cart'),
]