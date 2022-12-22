from django.db import models
from datetimemixin.models import DateTimeMixin
from products.models import Product
from shops.models import Shop
import secrets


# discount on single products using code/ discount by percentage

class DiscountCode(DateTimeMixin):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    code = models.CharField(max_length=30, unique=True)
    available_until = models.DateTimeField()
    amount = models.PositiveIntegerField(blank=True, null=True)
    percent = models.PositiveIntegerField(default=0)
    discount_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    sku = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(DiscountCode, self).save(*args, **kwargs)

