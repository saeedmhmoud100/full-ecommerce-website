from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.shortcuts import redirect
from django.utils import timezone 
# Create your models here.

class Post(models.Model):
    Posuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post',verbose_name='User')
    PostImg = models.ImageField(upload_to='blog_images',default='default.jpg',blank=True, null=True)
    Postitle = models.CharField(max_length=100,verbose_name='Title')
    Possubject = models.TextField(verbose_name='Subject')
    Posadd = models.DateTimeField(default=timezone.now,verbose_name='Add at')
    Posupdate = models.DateTimeField(auto_now=True, verbose_name='Update at')

    def post_img(self):
        if self.PostImg:
            return format_html(
                "<img src='{}'  width='50' height='50' />",
                self.PostImg.url,
            )
        else:
            return self.PostImg

    @property
    def short_subject(self):
        return truncatechars(self.Possubject, 150)

    @property
    def short_title(self):
        return truncatechars(self.Postitle,80)

    class Meta():
        ordering = ['-id']
    def __str__(self):
        return self.Postitle

class PostComment(models.Model):
    PCompost = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment',verbose_name='Post')
    PComuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment',verbose_name='User')
    PComessage = models.TextField(verbose_name='Message')
    PComadd = models.DateTimeField(default=timezone.now,verbose_name='Add at')
    PComupdate = models.DateTimeField(auto_now=True,verbose_name='Update at')


    def short_message(self):
        return truncatechars(self.PComessage,80)

    def __str__(self):
        return f'coment numper {self.pk} in {self.PCompost} post'
        
    class Meta():
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('blog-item-photo', args=[self.PCompost.pk])



class video(models.Model):
    Posvuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postvideo',verbose_name='User')
    posvimg = models.ImageField(upload_to='postvideo_img',default='default.jpg',blank=True, null=True,verbose_name='Img')
    PosvId = models.CharField(max_length=200,verbose_name='Video')
    Posvtitle = models.CharField(max_length=100,verbose_name='Title')
    Posvsubject = models.TextField(verbose_name='Subject')
    Posvadd = models.DateTimeField(default=timezone.now,verbose_name='Add at')
    Posvupdate = models.DateTimeField(auto_now=True, verbose_name='Update at')

    @property
    def short_subject(self):
        return truncatechars(self.Posvsubject, 150)

    @property
    def short_title(self):
        return truncatechars(self.Posvtitle,80)

    class Meta():
        ordering = ['-id']
    def __str__(self):
        return self.Posvtitle



class PostVideoComment(models.Model):
    PVCompost = models.ForeignKey(video, on_delete=models.CASCADE,related_name='videocomment',verbose_name='comment')
    PVComuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name='videocomment',verbose_name='User')
    PVComessage = models.TextField(verbose_name='Message')
    PVComadd = models.DateTimeField(default=timezone.now,verbose_name='Add at')
    PVComupdate = models.DateTimeField(auto_now=True,verbose_name='Update at')


    def short_message(self):
        return truncatechars(self.PVComessage,80)

    def __str__(self):
        return f'coment numper {self.pk} in {self.PVCompost} post'
        
    class Meta():
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('blog-item-video', args=[self.PVCompost.pk])



class BlogReview(models.Model):
    headertext = models.CharField(max_length=25)
    headertitle = models.CharField(max_length=100)
    itemvideourl = models.CharField(max_length=100)
    headerimg = models.ImageField(upload_to='blog-review-img')
    price = models.IntegerField()

    reviewimg1 = models.ImageField(upload_to='blog-review_img')
    reviewtitle1 = models.CharField(max_length=30)
    reviewdescription1 = models.TextField()

    reviewimg2 = models.ImageField(upload_to='blog-review_img')
    reviewtitle2 = models.CharField(max_length=30)
    reviewdescription2 = models.TextField()

    reviewimg3 = models.ImageField(upload_to='blog-review_img')
    reviewtitle3 = models.CharField(max_length=30)
    reviewdescription3 = models.TextField()

    createat = models.DateTimeField(auto_now=timezone.now)
    updateat = models.DateTimeField(auto_now=True,verbose_name='Update at')

    def __str__(self):
        return self.headertitle