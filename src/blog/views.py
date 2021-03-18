from django.shortcuts import render
# Create your views here.

def blog(request):
    return render(request,'ecommerce/blog.html')

def blog_item_video(request):
    return render(request,'ecommerce/blog-item-video.html')

def blog_item_review(request):
    return render(request,'ecommerce/blog-item-review.html')

def blog_item_photo(request):
    return render(request,'ecommerce/blog-item-photo.html')
