from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView,ListView,DetailView,UpdateView,DeleteView,CreateView,FormView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post,PostComment,video,PostVideoComment,BlogReview
from .forms import ItemPhotoPostForm,ItemPhotoCommentForm,ItemVideoCommentForm,ItemvideoPostForm
# Create your views here.



class HomeBlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 4

def blogfilter(request,data=None):
    if data == 'photo':
        contact_list = Post.objects.all()
    elif data == 'video':
        contact_list = video.objects.all()
    elif data == 'review':
        contact_list = BlogReview.objects.all()
    else:
        contact_list = [p for p in Post.objects.all()]
        contact_list += [v for v in video.objects.all()]
        contact_list += [b for b in BlogReview.objects.all()]
    paginator = Paginator(contact_list, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
        'page_obj': page_obj,
        'post_list':contact_list
    }
    return render(request,'blog/blog.html',context)

@login_required(login_url='login')
def itemphotocreatepost(request):
    if request.method == 'POST':
        new_post = ItemPhotoPostForm(request.POST, request.FILES)
        save = new_post.save(commit=False)
        save.Posuser = request.user
        save.save()
        messages.success(request,'added post successfuly!!')
        return redirect('blog')
    else:
        new_post = ItemPhotoPostForm()
    context ={
        'form':new_post,
        'title':'New Post',
        'h1':'Add New Post',
        'button':'Add Post',
    }
    return render(request, 'blog/Create_update_post.html',context)

class UpdatePostPhotItedView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class= ItemPhotoPostForm
    template_name = 'blog/Create_update_post.html'

    def get_context_data(self, **kwargs):
        context = super(UpdatePostPhotItedView, self).get_context_data(**kwargs)
        context['title'] = 'Update Post'
        context['h1'] = 'Update Post'
        context['button'] = 'Update Post'
        return context
    
    def form_valid(self,form):
        form.instance.Posuser = self.request.user
        form.save()
        messages.success(self.request,'updated post successfuly!!')
        return redirect(reverse('blog-item-photo',kwargs={'pk':form.instance.pk}))

class DeletePostItemPhotoView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'blog/item_photo_comment_delete.html'

    def get_context_data(self, **kwargs):
        context = super(DeletePostItemPhotoView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.object.id)
        context['item'] = 'Post'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request,'Deleted Post successfully!!')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog')

class ItemPhotoBlogView(DetailView, FormMixin):
    model = Post
    template_name = 'blog/blog-item-photo.html'
    context_object_name = 'post'
    form_class = ItemPhotoCommentForm

    def get_context_data(self, **kwargs):
        context = super(ItemPhotoBlogView, self).get_context_data(**kwargs)
        context['comments'] = PostComment.objects.filter(PCompost=self.object)
        context['form'] = ItemPhotoCommentForm()
        return context

    
    def get_success_url(self):
        return reverse('blog-item-photo',args=[self.object.id])
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/account/login/?next=/blog/itemphoto/{self.get_object().pk}')
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form_save = form.save(commit=False)
        form_save.PCompost = self.object
        form_save.PComuser = self.request.user
        form_save.save()
        messages.success(self.request,'Yor message added successfully!!')
        return super(ItemPhotoBlogView, self).form_valid(form)

class ItemPhotoUpdateCommentView(LoginRequiredMixin,UpdateView):
    template_name = 'blog/blog-item-photo.html'
    model = PostComment
    form_class = ItemPhotoCommentForm
    def get_context_data(self, **kwargs):
        context = super(ItemPhotoUpdateCommentView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.object.PCompost.id)
        context['comments'] = PostComment.objects.filter(PCompost=self.object.PCompost.id)
        context['changecomment']= 'Update Comment'
        return context

class ItemPhotoDeleteCommentView(LoginRequiredMixin,DeleteView):
    model = PostComment
    template_name = 'blog/item_photo_comment_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ItemPhotoDeleteCommentView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.object.PCompost.id)
        context['item'] = 'Comment'
        return context

    def get_success_url(self):
        return reverse('blog-item-photo',args=[self.object.PCompost.id])

class VideoBlogView(DetailView, FormMixin):
    model = video
    template_name = 'blog/blog-item-video.html'
    context_object_name = 'video'
    form_class = ItemPhotoCommentForm

    def get_context_data(self, **kwargs):
        context = super(VideoBlogView, self).get_context_data(**kwargs)
        context['comments'] = PostVideoComment.objects.filter(PVCompost=self.object.id)
        context['form'] = ItemVideoCommentForm()
        context['post'] = self.object
        return context

    
    def get_success_url(self):
        return reverse('blog-item-video',args=[self.object.id])

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/account/login/?next=/blog/blogitemvideo/{self.get_object().pk}')
        self.object = self.get_object()
        form = ItemVideoCommentForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form_save = form.save(commit=False)
        form_save.PVCompost = self.object
        form_save.PVComuser = self.request.user
        form_save.save()

        messages.success(self.request,'Yor message added successfully!!')
        return super(VideoBlogView, self).form_valid(form)

class UpdateVideoCommentView(LoginRequiredMixin,UpdateView):
    template_name = 'blog/blog-item-video.html'
    model = PostVideoComment
    form_class = ItemVideoCommentForm
    def get_context_data(self, **kwargs):
        context = super(UpdateVideoCommentView, self).get_context_data(**kwargs)
        context['video'] = video.objects.get(pk=self.object.PVCompost.id)
        context['comments'] = PostVideoComment.objects.filter(PVCompost=self.object.PVCompost.id)
        context['changecomment']= 'Update Comment'
        return context

class DeleteVideoCommentView(LoginRequiredMixin,DeleteView):
    model = PostVideoComment
    template_name = 'blog/item_photo_comment_delete.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteVideoCommentView, self).get_context_data(**kwargs)
        context['post'] = video.objects.get(pk=self.object.PVCompost.id)
        context['item'] = 'Comment'
        return context

    def get_success_url(self):
        return reverse('blog-item-video',args=[self.object.PVCompost.id])

def blog_item_review(request,id):
    item_review = BlogReview.objects.get(id=id)
    context={
        'item':item_review
    }
    return render(request,'blog/blog-item-review.html',context)

class UpdatePostvideoView(LoginRequiredMixin,UpdateView):
    model = video
    form_class= ItemvideoPostForm
    template_name = 'blog/Create_update_post.html'

    def get_context_data(self, **kwargs):
        context = super(UpdatePostvideoView, self).get_context_data(**kwargs)
        context['title'] = 'Update Post'
        context['h1'] = 'Update Post'
        context['button'] = 'Update Post'
        return context
    
    def form_valid(self,form):
        form.instance.Posvuser = self.request.user
        form.save()
        messages.success(self.request,'updated post successfuly!!')
        return redirect(reverse('blog-item-video',kwargs={'pk':form.instance.pk}))

class DeletePostItemVideoView(LoginRequiredMixin,DeleteView):
    model = video
    template_name = 'blog/item_photo_comment_delete.html'

    def get_context_data(self, **kwargs):
        context = super(DeletePostItemVideoView, self).get_context_data(**kwargs)
        context['post'] = video.objects.get(pk=self.object.id)
        context['item'] = 'Post'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request,'Deleted Post successfully!!')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog-item', kwargs={'data':'video'})


