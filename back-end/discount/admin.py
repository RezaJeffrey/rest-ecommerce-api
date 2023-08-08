from django.contrib import admin
from .models import ProductDiscount, DiscountCode

admin.site.register(DiscountCode)
admin.site.register(ProductDiscount)

