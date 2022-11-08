from django.contrib import admin
from products import models
from extra_fields.admin import ValueInline


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ValueInline
    ]


admin.site.register(models.Product, ProductAdmin)