from django.contrib import admin
from carts.models import CartItem, Cart
from productpacks.models import ProductPack


class CartItemInline(admin.StackedInline):
    model = CartItem
    fields = [
        'cart', 'item',
        'quantity', 'price'
    ]


class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]


admin.site.register(Cart, CartAdmin)









