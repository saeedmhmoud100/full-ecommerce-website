from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from PIL import Image  
from user.models import Customer
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
    ('Business','Business'),
    ('Home','Home'),
    ('Mobility','Mobility'),
    ('Powerfull','Powerfull'),
    ('Gaming','Gaming')
)

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30,verbose_name='Title')
    discrption = models.TextField(verbose_name='Discrption')
    img = models.ImageField(upload_to='product_img',verbose_name='Img')
    video_img = models.ImageField(upload_to='product_video_img',blank=True, null=True,verbose_name='Video Img')
    video_id = models.CharField(max_length=20,blank=True, null=True,verbose_name='Youtube Video Id')
    Brand = models.CharField(max_length=20,choices=PRODUCT_BRAND,verbose_name='Brand')
    prodtype = models.CharField(max_length=15,choices=PRODUCT_TYPE,verbose_name='Product type')
    os = models.CharField(max_length=20,verbose_name='Operating system')
    Process_type = models.CharField(max_length=20,verbose_name='Processor type')
    Graphic_quality = models.CharField(max_length=20,verbose_name='Graphics')
    screen_size = models.IntegerField(default=0,verbose_name='Screen Size')
    tag1 = models.CharField(max_length=20,choices=PRODUCT_MADE_FOR,verbose_name='Tags')
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


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='cart')
    quantity = models.PositiveIntegerField(default=1)
    amount = models.FloatField(blank=True)

    def save(self,*args,**kwargs):
        total = 0
        if self.product.discount_price:
            total = self.product.discount_price * self.quantity
        else:
            total = self.product.selling_price * self.quantity
        self.amount = total
        super(Cart,self).save(*args,**kwargs)
    def __str__(self):
        return f'{self.product.title} product of {self.user.username} user'



VIDEO_SOURCE = (
    ('youtube','youtube'),
    ('vimeo','Vimeo')
)
class Gallery(models.Model):
    title = models.CharField(max_length=50,verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    img = models.ImageField(upload_to='gellary_img',verbose_name='Image')
    video = models.CharField(max_length=50,verbose_name='or Video Id',default=' ')
    source = models.CharField(max_length=10,choices=VIDEO_SOURCE,default='youtube',verbose_name='Video source')
    @property
    def img_url(self):
        return self.img.url
    def __str__(self):
        return self.title

ORDER_STATE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cansel','Cansel'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    delevery_option= models.CharField(max_length=50) 
    payment = models.CharField(max_length=40)
    remark = models.TextField(blank=True, null=True)
    order_data = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=30,choices=ORDER_STATE,default='panding')

    def __str__(self):
        return f'order of {self.user} user'