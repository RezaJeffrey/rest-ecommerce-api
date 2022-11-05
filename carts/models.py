import secrets

from django.db import models
from datetimemixin.models import DateTimeMixin
from django.contrib.auth import get_user_model
from products.models import Product
from extra_fields.models import ExtraFieldValue, ExtraFieldName

User = get_user_model()

"""
class Pack(DateTimeMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='paks',
        blank=False,
    )
    extra_field_names = models.ForeignKey(
        ExtraFieldName,
        related_name='paks',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    extra_field_values = models.ForeignKey(
        ExtraFieldValue,
        related_name="paks",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    sku = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        unique=True
    )

    class Meta:
        unique_together = ['extra_field_names', 'extra_field_values']

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(Pack, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.product


class Cart(DateTimeMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="carts",
        blank=False
    )
    packs = models.ManyToManyField(
        Pack,
        related_name="carts",
        blank=False,
    )
    sku = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(Cart, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user
"""