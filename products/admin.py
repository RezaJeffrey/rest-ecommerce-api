from django.contrib import admin
from products import models

admin.site.register(models.Shop)
admin.site.register(models.Brand)
admin.site.register(models.ShopAddress)


# admin.site.register(models.Product)
# admin.site.register(models.ProductImage)
# admin.site.register(models.Comment)
# admin.site.register(models.ExtraFieldName)
# admin.site.register(models.ExtraFieldValue)
# admin.site.register(models.ReplyComment)
# admin.site.register(models.LikeComment)

class ProductImageInline(admin.TabularInline):
    model = models.ProductImage


class ValueInLine(admin.TabularInline):
    model = models.ExtraFieldValue


class ExtraFieldAdmin(admin.ModelAdmin):
    inlines = [
        ValueInLine,
    ]


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ValueInLine
    ]


admin.site.register(models.ExtraFieldName, ExtraFieldAdmin)
admin.site.register(models.Product, ProductAdmin)