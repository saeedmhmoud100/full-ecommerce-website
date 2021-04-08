from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.http import JsonResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from ecommerce.models import Order
from.forms import RegisterForm,ProfileRegisterForm,LoginForm,AddLocationForm
from .models import Customer,UserProfile
# Create your views here.


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile',username=request.user)
        form = RegisterForm()
        proform = ProfileRegisterForm()
        return render(request, 'user/signup.html',{'form':form,'proform':proform})
    def post(self,request):
        form = RegisterForm(request.POST)
        proform = ProfileRegisterForm(request.POST)
        if form.is_valid() and proform.is_valid():
            form_save = form.save(commit=False)
            form_save.set_password(form.cleaned_data['password1'])
            form_save.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            profilephone = proform.cleaned_data['phone']
            UserProfile.objects.create(user=user,CustPhone=profilephone)
            messages.success(request, 'Successfully registration!!')
            return redirect('login')
        
        
        return render(request,'user/signup.html',{'form':form,'proform':proform})

def login(request):
    if request.user.is_authenticated:
        return redirect('profile',username=request.user)
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username,password=password)
        red = request.GET.get('next')
        
        if user is not None:
            auth_login(request,user)
            if red:
                return HttpResponseRedirect(red)
            else:
                return redirect(reverse('profile', kwargs={'username': username}))
    else:
        form = LoginForm()
    return render(request,'user/login.html',{'form':form})

class ProfileView(LoginRequiredMixin,View):
    def get(self,request,username):
        if username != request.user.username:
            return redirect('profile',username=request.user)
        proform = UserProfile.objects.get(user__username=username)
        locationform = AddLocationForm()
        locations = Customer.objects.filter(user__username=username).order_by('-id')
        orders = Order.objects.filter(user=request.user)
        context = {
            'profile':proform,
            'locform':AddLocationForm,
            'locations':locations,
            'orders':orders
            }
        return render(request, 'user/profile.html',context)
    def post(self,request,username):
        proform = UserProfile.objects.get(user=request.user)
        locationform = AddLocationForm(request.POST)
        locations = Customer.objects.filter(user=request.user)
        user = User.objects.get(username=request.user)
        if locationform.is_valid():
            form_save = locationform.save(commit=False)
            form_save.user = request.user
            form_save.save()
            messages.success(request, 'add location successfully!! ')
            return HttpResponseRedirect(f'/account/profile/{user}')

        return render(request, 'user/profile.html',{'profile':proform,'locform':AddLocationForm,'locations':locations})

@login_required(login_url='login')
def delete_location(request,pk):
    loc_id = request.GET.get('id')
    Customer.objects.filter(id=loc_id).delete()
    return JsonResponse({'data':'yes'})


