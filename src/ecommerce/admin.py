from django.contrib import admin
from .models import Product,ProductProperty,productComment,ProductImg

admin.site.register(Product)
admin.site.register(ProductProperty)
admin.site.register(productComment)
admin.site.register(ProductImg)