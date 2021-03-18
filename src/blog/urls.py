from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeBlogView.as_view(),name='blog'),
    path('blogitemvideo/',views.blog_item_video,name='blog-ite-video'),
    path('blogitemreview/',views.blog_item_review,name='blog-item-review'),
    path('itemphoto/<int:id>',views.blog_item_photo,name='blog-item-photo'),
]