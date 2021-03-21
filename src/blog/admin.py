from django.contrib import admin
from .models import Post, PostComment,video,PostVideoComment,BlogReview
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Posuser','post_img','short_title','short_subject','Posadd','Posupdate']
    

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['PCompost','PComuser','short_message','PComadd','PComupdate']


@admin.register(video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['Posvuser','short_title','short_subject','Posvadd','Posvupdate']
    

@admin.register(PostVideoComment)
class PostVideoCommentAdmin(admin.ModelAdmin):
    list_display = ['PVCompost','PVComuser','short_message','PVComadd','PVComupdate']


admin.site.register(BlogReview)