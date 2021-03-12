from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from.forms import RegisterForm,LoginForm
# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/signup.html',{'form':form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.set_password(form.cleaned_data['password1'])
            form_save.save()
            messages.success(request, 'Successfully registration!!')
            return redirect('login')
        
        return render(request,'user/signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('register')
    else:
        form = LoginForm()
    return render(request,'user/login.html',{'form':form})