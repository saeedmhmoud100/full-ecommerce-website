from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
from django.utils import timezone 
# Create your models here.

class Post(models.Model):
    Posuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post',verbose_name='User')
    PostImg = models.ImageField(upload_to='blog_images')
    Postitle = models.CharField(max_length=100,verbose_name='Title')
    Possubject = models.TextField(verbose_name='Subject')
    Posadd = models.DateTimeField(default=timezone.now,verbose_name='Add at')
    Posupdate = models.DateTimeField(auto_now=True, verbose_name='Update at')

    def post_img(self):
        return format_html(
            "<img src='{}'  width='50' height='50' />",
            self.PostImg.url,
        )

    @property
    def short_subject(self):
        return truncatechars(self.Possubject, 150)

    @property
    def short_title(self):
        return truncatechars(self.Postitle,80)

    def __str__(self):
        return self.Postitle

class PostComment(models.Model):
    PCompost = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment',verbose_name='Post')
    PComuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment',verbose_name='User')
    PComtitle = models.CharField(max_length=100,verbose_name='Title')
    PComessage = models.TextField(verbose_name='Message')
    PComadd = models.DateTimeField(default=timezone.now,verbose_name='Add at')
    PComupdate = models.DateTimeField(auto_now=True,verbose_name='Update at')

    def __str__(self):
        return self.PComtitle