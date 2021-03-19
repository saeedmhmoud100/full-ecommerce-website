from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeBlogView.as_view(),name='blog'),
    path('newpostitemphoto/',views.itemphotocreatepost,name = 'add-post-item-photo'),
    path('updatepostitemphoto/<int:pk>/',views.UpdatePostPhotItedView.as_view(),name = 'update-post-item-photo'),
    path('deletepostitemphoto/<int:pk>/',views.DeletePostItemPhotoView.as_view(),name = 'delete-post-item-photo'),
    path('itemphoto/<int:pk>/',views.ItemPhotoBlogView.as_view(),name='blog-item-photo'),
    path('itemphoto/updatecomment/<int:pk>/',views.ItemPhotoUpdateCommentView.as_view(),name='blog-item-photo-update'),
    path('itemphoto/deletecomment/<int:pk>/',views.ItemPhotoDeleteCommentView.as_view(),name='blog-item-photo-delete'),
    path('blogitemvideo/',views.blog_item_video,name='blog-ite-video'),
    path('blogitemreview/',views.blog_item_review,name='blog-item-review'),
    
]