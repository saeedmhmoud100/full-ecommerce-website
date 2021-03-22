from django.contrib import admin
from .models import Product,Product_property,product_comments

admin.site.register(Product)
admin.site.register(Product_property)
admin.site.register(product_comments)