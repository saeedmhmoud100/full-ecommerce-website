from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
# Create your models here.

PRODUCT_TYPE =  (
    ('laptop','Laptops'),
    ('taplet','Taplet'),
    ('hybrid','Hybrid')
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
    img = models.ImageField(upload_to='product_img',verbose_name='Img')
    Brand = models.CharField(max_length=20,choices=PRODUCT_BRAND,verbose_name='Brand')
    prodtype = models.CharField(max_length=15,choices=PRODUCT_TYPE,verbose_name='Product type')
    os = models.CharField(max_length=20,verbose_name='Operating system')
    Process_type = models.CharField(max_length=20,verbose_name='Processor type')
    Graphic_quality = models.CharField(max_length=20,verbose_name='Graphics')
    screen_size = models.IntegerField(default=0,verbose_name='Screen Size')
    tag1 = models.CharField(max_length=20,choices=PRODUCT_MADE_FOR,verbose_name='Tags')
    tag2 = models.CharField(max_length=20,choices=PRODUCT_MADE_FOR,verbose_name='Tags',blank=True, null=True)
    tag3 = models.CharField(max_length=20,choices=PRODUCT_MADE_FOR,verbose_name='Tags',blank=True, null=True)
    selling_price = models.FloatField(default=0,verbose_name='Selling Price')
    discount_price = models.FloatField(default=0,verbose_name='Discount Price',blank=True, null=True)
    favourites = models.ManyToManyField(User,default=None,blank=True,related_name='favourite')
    created_at= models.DateTimeField(default=timezone.now,verbose_name='Created At')
    update_at = models.DateTimeField(auto_now_add=True,verbose_name='Update At')


    def __str__(self):
        return self.title

class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='imgs')
    img = models.ImageField(upload_to='product_img',verbose_name='Img')


    def __str__(self):
        return f'{self.product.title} img'
class ProductProperty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='property')
    prop = models.CharField(max_length=25,verbose_name='Property')
    prop_discrption = models.CharField(max_length=250,verbose_name='discrption of the Proprty')
    
    def __str__(self):
        return f'{self.product.title} property'
    
class productComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comment')
    message = models.TextField(verbose_name='Message')
    created_at= models.DateTimeField(default=timezone.now,verbose_name='Created At')

    def __str__(self):
        return f'comment of {self.user.username} on {self.product.title} product'