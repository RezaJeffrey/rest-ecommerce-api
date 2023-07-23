from datetimemixin.models import DateTimeMixin
from django.db import models
import secrets
from django.contrib.auth import get_user_model
User = get_user_model()


class ShopAddress(DateTimeMixin):
    address = models.CharField(max_length=500, unique=True)
    postal_code = models.PositiveBigIntegerField(blank=True, null=True, unique=True)  # TODO postal code iran format(max, min length)
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(ShopAddress, self).save(*args, **kwargs)

    def __str__(self):
        return self.address[:35]


class Shop(DateTimeMixin):
    name = models.CharField(max_length=255)
    province = models.CharField(max_length=120)  # TODO choicefields for province
    address = models.OneToOneField(ShopAddress, on_delete=models.SET_NULL, blank=True, null=True)
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(Shop, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ShopStaf(DateTimeMixin):
    user = models.ForeignKey(User, related_name="shopstafs", on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name="shopstafs", on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(ShopStaf, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.staf.name}  -- > staf_of: {self.shop.name}"
