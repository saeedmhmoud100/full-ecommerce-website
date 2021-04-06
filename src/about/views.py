from django.shortcuts import render,redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from .models import FaqQuestion
# Create your views here.



class FAQView(View):
    def get(self, request,*arge,**kwargs):
        page = int(request.GET.get('page',1))
        question_numper = 3
        firstquestion = FaqQuestion.objects.all()[page*question_numper-question_numper:page*question_numper]
        lastquestion = FaqQuestion.objects.all().order_by('-id')[page*question_numper-question_numper:page*question_numper]
        contact_list = FaqQuestion.objects.all()
        paginator = Paginator(contact_list, question_numper)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context= {
            'page_obj':page_obj,
            'first_question':firstquestion,
            'last_question':lastquestion
        }
        return render(request,'about/faq.html',context)
    def post(self,request,*args,**kwargs):
        message = request.POST['message']
        email = request.POST['email']
        if request.user.is_authenticated:
            if User.objects.filter(email=email).exists():
                FaqQuestion(user=request.user,question=message).save()
                messages.success(request,'added question successfully!!')
            else:
                messages.warning(request,'the email is not valid')
                return redirect('faq')
        else:
            return redirect('login')
        return redirect('faq')

def contacts(request):
    return render(request,'about/contacts.html')


