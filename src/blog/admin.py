from django.contrib import admin
from .models import Post, PostComment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Posuser','post_img','short_title','short_subject','Posadd','Posupdate']
    

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['PCompost','PComuser','PComtitle','PComessage','PComadd','PComupdate']