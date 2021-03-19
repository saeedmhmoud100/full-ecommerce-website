from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import UpdateView,ListView,DetailView,UpdateView,DeleteView,CreateView,FormView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from .models import Post,PostComment
from .forms import ItemPhotoPostForm,ItemPhotoCommentForm
# Create your views here.



class HomeBlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 2


#try create with class based view
# class ItemPhotoCreatePostView(FormView,FormMixin):
#     model = Post
#     form_class = ItemPhotoPostForm
#     template_name = 'blog/Create_update_post.html'

#     def get_context_data(self, **kwargs):
#         context = super(ItemPhotoCreatePostView, self).get_context_data(**kwargs)
#         context['title'] = 'New Post'
#         context['h1'] = 'Add New Post'
#         context['button'] = 'Add Post'
#         return context

#     def form_valid(self, form):
#         print(self.object)
#         print(self.object.id)
#         form.save()
#         messages.success(request,'added post successfuly!!')
#         return super(ItemPhotoCreatePostView, self).form_valid(form)

# def post(self, request, *args, **kwargs):
#     self.object = self.get_object()
#     form = self.get_form()
#     if form.is_valid():
#         return self.form_valid(form)
#     else:
#         return self.form_invalid(form)

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().get(request, *args, **kwargs)

#     def get_success_url(self):
        
#         return reverse('blog')

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

class UpdatePostPhotItedView(UpdateView):
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

class DeletePostItemPhotoView(DeleteView):
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

class ItemPhotoUpdateCommentView(UpdateView):
    template_name = 'blog/blog-item-photo.html'
    model = PostComment
    form_class = ItemPhotoCommentForm
    def get_context_data(self, **kwargs):
        context = super(ItemPhotoUpdateCommentView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.object.PCompost.id)
        context['comments'] = PostComment.objects.filter(PCompost=self.object.PCompost.id)
        context['changecomment']= 'Update Comment'
        return context

class ItemPhotoDeleteCommentView(DeleteView):
    model = PostComment
    template_name = 'blog/item_photo_comment_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ItemPhotoDeleteCommentView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.object.PCompost.id)
        context['item'] = 'Comment'
        return context

    def get_success_url(self):
        return reverse('blog-item-photo',args=[self.object.PCompost.id])


def blog_item_review(request):
    return render(request,'ecommerce/blog-item-review.html')


def blog_item_video(request):
    return render(request,'ecommerce/blog-item-video.html')
