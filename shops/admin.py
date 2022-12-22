from django.contrib import admin
from shops import models


admin.site.register(models.Shop)
admin.site.register(models.ShopAddress)
admin.site.register(models.ShopStaf)
