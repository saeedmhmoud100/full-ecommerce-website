from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('catalog/',views.CatalogView.as_view(),name='catalog'),
    path('catalogproduct/<int:pk>',views.CatalogProductView.as_view(),name='catalog-product'),
    path('gallery/',views.gallery,name='gallery'),
    path('faq/',views.faq,name='faq'),
    path('contacts/',views.contacts,name='contacts'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/',views.cart,name='cart'),
]