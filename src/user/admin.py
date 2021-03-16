from django.contrib import admin
from .models import Customer,UserProfile
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display= ['id','CustCountry','CustCity','CustLocality','CustZipcode']


admin.site.register(UserProfile)