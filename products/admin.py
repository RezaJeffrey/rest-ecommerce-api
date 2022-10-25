from django.contrib import admin
from products import models

admin.site.register(models.Shop)
admin.site.register(models.Brand)
admin.site.register(models.ShopAddress)
admin.site.register(models.Product)
admin.site.register(models.ExtraFieldName)


# admin.site.register(models.Comment)
# admin.site.register(models.ExtraFieldName)
# admin.site.register(models.ExtraFieldValue)
# admin.site.register(models.ReplyComment)
# admin.site.register(models.LikeComment)

class ProductImageInline(admin.TabularInline):
    model = models.ProductImage


class ProductInLine(admin.TabularInline):
    model = models.ProductIventoryValue


class ExtraFieldAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]


class ExtraFieldValueAdmin(admin.ModelAdmin):
    inlines = [
        # ProductImageInline,
        ProductInLine,
    ]


admin.site.register(models.ExtraFieldValue, ExtraFieldAdmin)
admin.site.register(models.ProductInventory, ExtraFieldValueAdmin)
