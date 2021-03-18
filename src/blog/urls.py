from django.urls import path
from . import views
urlpatterns = [
    path('blog/',views.blog,name='blog'),
    path('blogitemvideo/',views.blog_item_video,name='blog-ite-video'),
    path('blogitemreview/',views.blog_item_review,name='blog-item-review'),
    path('blogitemphoto/',views.blog_item_photo,name='blog-item-photo'),
]