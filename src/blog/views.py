from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.



class HomeBlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 2


# def blog(request):
#     return render(request,'ecommerce/blog.html')

def blog_item_video(request):
    return render(request,'ecommerce/blog-item-video.html')

def blog_item_review(request):
    return render(request,'ecommerce/blog-item-review.html')

def blog_item_photo(request):
    return render(request,'ecommerce/blog-item-photo.html')
