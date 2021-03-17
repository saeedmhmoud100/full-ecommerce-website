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
    path('blog/',views.blog,name='blog'),
    path('blogitemvideo/',views.blog_item_video,name='blog-ite-video'),
    path('blogitemreview/',views.blog_item_review,name='blog-item-review'),
    path('blogitemphoto/',views.blog_item_photo,name='blog-item-photo'),
]