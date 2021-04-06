from django.shortcuts import render
from django.views.generic import View
# Create your views here.



class FAQView(View):
    def get(self, request,*arge,**kwargs):
        return render(request,'about/faq.html')


def contacts(request):
    return render(request,'about/contacts.html')


