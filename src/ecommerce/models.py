from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
# Create your models here.

PRODUCT_TYPE =  (
    ('lap','Laptops'),
    ('tap','Taplet'),
    ('hyp','Hybrid')
)
PRODUCT_BRAND = (
    ('hp','HP'),
    ('asus','ASUS'),
    ('lenovo','Lenovo'),
    ('apple','Apple')
)
PRODUCT_MADE_FOR = (
    ('busi','Business'),
    ('home','Home'),
    ('mobil','Mobility'),
    ('power','Powerfull'),
    ('game','Gaming')
)

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30,verbose_name='Title')
    discrption = models.TextField(verbose_name='Discrption')
    Brand = models.CharField(max_length=20,choices=PRODUCT_BRAND,verbose_name='Brand')
    prodtype = models.CharField(max_length=15,choices=PRODUCT_TYPE,verbose_name='Product type')
    os = models.CharField(max_length=20,verbose_name='Operating system')
    Process_type = models.CharField(max_length=20,verbose_name='Processor type')
    Graphic_quality = models.CharField(max_length=20,verbose_name='Graphics')
    screen_size = models.IntegerField(default=0,verbose_name='Screen Size')
    tag1 = models.CharField(max_length=20,choices=PRODUCT_MADE_FOR,verbose_name='Tags')
    tag2 = models.CharField(max_length=20,choices=PRODUCT_MADE_FOR,verbose_name='Tags',blank=True, null=True)
    tag3 = models.CharField(max_length=20,choices=PRODUCT_MADE_FOR,verbose_name='Tags',blank=True, null=True)
    selling_price = models.IntegerField(default=0,verbose_name='Selling Price')
    discount_price = models.IntegerField(default=0,verbose_name='Discount Price')
    created_at= models.DateTimeField(default=timezone.now,verbose_name='Created At')
    update_at = models.DateTimeField(auto_now_add=True,verbose_name='Update At')

class Product_property(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prop')
    prop = models.CharField(max_length=25,verbose_name='Proprty')
    prop_discrption = models.CharField(max_length=250,verbose_name='discrption of the Proprty')

class product_comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Message')
    created_at= models.DateTimeField(default=timezone.now,verbose_name='Created At')
