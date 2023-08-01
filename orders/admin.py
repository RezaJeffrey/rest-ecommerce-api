from django.contrib import admin
from orders.models import OrderStatus, Order


class OrderAdminTabular(admin.TabularInline):
    model = OrderStatus


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderAdminTabular
    ]


admin.site.register(Order, OrderAdmin)
