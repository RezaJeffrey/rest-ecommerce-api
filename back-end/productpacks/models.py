from products.models import Product
from extra_fields.models import ExtraFieldValue
from datetimemixin.models import DateTimeMixin
from django.db import models
from django.contrib.auth import get_user_model
from shops.models import Shop
import secrets


User = get_user_model()


class ProductPack(DateTimeMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="paks",
        blank=False
    )
    extra_field_values = models.ManyToManyField(
        ExtraFieldValue,
        related_name="paks",
        blank=True,
    )
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE, related_name="packs", blank=False, null=True)
    stock = models.IntegerField(default=0)
    # TODO remove the default value (add to test only)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(ProductPack, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name
