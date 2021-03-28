from django import forms
from .models import productComment

class ProductComment(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'4'}))
    class Meta:
        model = productComment
        fields = ('message',)