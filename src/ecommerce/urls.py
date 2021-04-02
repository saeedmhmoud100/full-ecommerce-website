from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('catalog/',views.CatalogView.as_view(),name='catalog'),
    path('catalogproduct/<int:pk>',views.CatalogProductView.as_view(),name='catalog-product'),
    path('addtocart/',views.add_to_cart,name='add-to-cart'),
    path('favorunfav/',views.favorite_or_unfavorite,name='fav'),
    path('catalog/fil', views.ProductFilterView.as_view(), name='catalog-filter'),
    path('cart/',views.CartView.as_view(),name='cart'),
    path('prusorminus/',views.plus_or_minus_cart,name='prus-or-minus'),
    path('removecart/',views.remove_cart,name='remove-cart'),
    path('gallery/',views.GalleryView.as_view(),name='gallery'),
    path('checkout/',views.checkout,name='checkout'),
]