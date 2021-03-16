from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from.forms import RegisterForm,ProfileRegisterForm,LoginForm
from .models import Customer,UserProfile
# Create your views here.


class RegisterView(View):
    def get(self, request):
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
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request,'user/login.html',{'form':form})

def profile(request):
    return render(request, 'user/profile.html')