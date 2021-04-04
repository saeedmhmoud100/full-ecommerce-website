from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from.forms import RegisterForm,ProfileRegisterForm,LoginForm,AddLocationForm
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
            return redirect(reverse('profile', kwargs={'username': username}))
    else:
        form = LoginForm()
    return render(request,'user/login.html',{'form':form})

class ProfileView(View):
    def get(self,request,username):
        proform = UserProfile.objects.get(user=request.user)
        locationform = AddLocationForm()
        locations = Customer.objects.filter(user=request.user)
        return render(request, 'user/profile.html',{'profile':proform,'locform':AddLocationForm,'locations':locations})
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

def locationdelete(request,pk,):
    cust= Customer.objects.get(id=pk)
    cust.delete()
    return redirect(reverse('profile',kwargs={'username':request.user}))
    return HttpResponseRedirect((f'profile/delete/{pk}'))

