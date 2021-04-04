from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    CustPhone = models.IntegerField(verbose_name='Phone')

    def __str__(self):
        return f'{self.user} Profile'

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    CustCountry = CountryField()
    CustCity = models.CharField(max_length=60,verbose_name='City')
    CustLocality= models.CharField(max_length=60,verbose_name='Locality')
    CustZipcode = models.CharField(max_length=15,verbose_name='Zipcode')
    


# @receiver(post_save, sender=User)
# def create_profile(sender, instance,created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)