from django.contrib import admin
from .models import FaqAnswer,FaqQuestion
# Register your models here.

admin.site.register(FaqQuestion)
admin.site.register(FaqAnswer)
