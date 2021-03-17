from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm,PasswordChangeForm
from .models import UserProfile,Customer
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','name':'username','placeholder':'User Name'}))
    email = forms.CharField(max_length=200,widget=forms.EmailInput(attrs={'class':'form-control','name':'email','placeholder':'E-mail'}))
    password1 = forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','name':'password1','placeholder':'Password'}))
    password2 = forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','name':'password2','placeholder':'Re-Password (agein)'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def clean_password2(self):

        cd = self.cleaned_data
        
        if cd['password1'] != cd['password2']:
            
            raise forms.ValidationError('Password not equal re.password')
            print('yes')
            return cd['password2']


    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('this name is alraly taken')
        return cd['username']

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('this email is alraly taken')
        return cd['email']

class ProfileRegisterForm(forms.ModelForm):
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','name':'phone','placeholder':'Phone'}))
    class Meta:
        model= UserProfile
        fields = ('phone',)

    def clean_phone(self):
        return self.cleaned_data['phone']

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control mb-3','name':'username','placeholder':'User Name','style':'margin-bottom:15px'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control mb-3','name':'password1','placeholder':'Password','style':'margin-bottom:15px'}))
    class Meta:
        model = User
        fields = ('username','password1')

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class':'form-control','name':'email','placeholder':'E-mail'}))

class SetResetePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(min_length=8,label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}))
    new_password2 = forms.CharField(min_length=8,label='New Password (agein)',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password(agein)'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(min_length=8,label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old Password'}))
    new_password1 = forms.CharField(min_length=8,label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}))
    new_password2 = forms.CharField(min_length=8,label='Re.New Password (agein)',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re.New Password (agein)'}))


class AddLocationForm(forms.ModelForm):
    CustCountry = forms.CharField(label='Country ',widget=forms.TextInput(attrs={'class':' mr-3','name':'country','placeholder':'Country','style':'margin-left:15px;margin-bottom:5px'}))
    CustCity = forms.CharField(label='City',widget=forms.TextInput(attrs={'class':' mr-3','name':'city','placeholder':'City','style':'margin-left:39px;margin-bottom:5px'}))
    CustLocality = forms.CharField(label='Locality',widget=forms.TextInput(attrs={'class':' mr-3','name':'locality','placeholder':'Locality','style':'margin-left:16px;margin-bottom:5px'}))
    CustZipcode = forms.CharField(max_length=10,label='Zipcode ',widget=forms.NumberInput(attrs={'class':' mr-3','name':'Zipcode','placeholder':'zipcode','style':'margin-left:15px;margin-bottom:5px'}))
    class Meta:
        model = Customer
        fields = ('CustCountry','CustCity','CustLocality','CustZipcode')
