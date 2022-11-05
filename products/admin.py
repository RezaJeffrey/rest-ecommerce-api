from django.contrib import admin
from products import models
from extra_fields.admin import ValueInline

admin.site.register(models.Shop)
admin.site.register(models.Brand)
admin.site.register(models.ShopAddress)


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ValueInline
    ]


admin.site.register(models.Product, ProductAdmin)