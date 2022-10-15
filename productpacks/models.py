from products.models import Product, ExtraFieldName, ExtraFieldValue
from datetimemixin.models import DateTimeMixin
from django.db import models
from django.contrib.auth import get_user_model
import secrets

User = get_user_model()


class ProductPack(DateTimeMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="paks",
        blank=False
    )
    extra_field_value = models.ForeignKey(
        ExtraFieldName,
        on_delete=models.CASCADE,
        related_name="paks",
        blank=False
    )
    sku = models.CharField(
        max_length=255,
        blank=False,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(self, ProductPack).save(*args, **kwargs)

    def __str__(self):
        return self.product



