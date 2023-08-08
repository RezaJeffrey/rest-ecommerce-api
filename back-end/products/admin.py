from django.contrib import admin
from products import models


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline
    ]


admin.site.register(models.Product, ProductAdmin)
