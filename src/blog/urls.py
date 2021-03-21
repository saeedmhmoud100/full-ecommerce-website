from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeBlogView.as_view(),name='blog'),
    path('blog/<slug:data>/',views.blogfilter,name='blog-item'),
    path('newpostitemphoto/',views.itemphotocreatepost,name = 'add-post-item-photo'),
    path('updatepostitemphoto/<int:pk>/',views.UpdatePostPhotItedView.as_view(),name = 'update-post-item-photo'),
    path('deletepostitemphoto/<int:pk>/',views.DeletePostItemPhotoView.as_view(),name = 'delete-post-item-photo'),
    path('itemphoto/<int:pk>/',views.ItemPhotoBlogView.as_view(),name='blog-item-photo'),
    path('itemphoto/updatecomment/<int:pk>/',views.ItemPhotoUpdateCommentView.as_view(),name='blog-item-photo-update'),
    path('itemphoto/deletecomment/<int:pk>/',views.ItemPhotoDeleteCommentView.as_view(),name='blog-item-photo-delete'),
    path('blogitemvideo/<int:pk>',views.VideoBlogView.as_view(),name='blog-item-video'),
    path('updatevideoitem/<int:pk>/',views.UpdateVideoCommentView.as_view(),name = 'update-video-item'),
    path('deletevideoitem/<int:pk>/',views.DeleteVideoCommentView.as_view(),name = 'delete-video-item'),
    path('updatepostitemvideo/<int:pk>/',views.UpdatePostvideoView.as_view(),name = 'update-post-item-video'),
    path('deletepostitemvideo/<int:pk>/',views.DeletePostItemVideoView.as_view(),name = 'delete-post-item-video'),
    path('blogitemreview/<int:id>',views.blog_item_review,name='blog-item-review'),
    
]