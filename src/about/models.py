from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FaqQuestion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.CharField(max_length=40,verbose_name='The question')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')

    def __str__(self):
        return self.question

class FaqAnswer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.OneToOneField(FaqQuestion, on_delete=models.CASCADE,related_name='answer')
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')

    def __str__(self):
        return f'anewer to {self.question} question'