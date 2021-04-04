from django import forms
from django_countries.widgets import CountrySelectWidget
from user.models import Customer
from .models import productComment

class ProductComment(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}))
    class Meta:
        model = productComment
        fields = ('message',)

class AddNewAddressForm(forms.ModelForm):
    CustCity = forms.CharField(max_length=30)
    CustLocality = forms.CharField(max_length=30)
    CustZipcode = forms.IntegerField()
    class Meta:
        model = Customer
        fields = ('CustCountry','CustCity','CustLocality','CustZipcode')
        widgets = {
            'CustCountry': CountrySelectWidget(attrs={'class':'form-control select'}),
            'CustCity':forms.TextInput(attrs={'class':'form-control input-sm'}),
            'CustLocality':forms.TextInput(attrs={'class':'form-control input-sm'}),
            'CustZipcode':forms.NumberInput(attrs={'class':'form-control input-sm'})
            
            }