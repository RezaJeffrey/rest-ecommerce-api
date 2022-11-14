from django.db import models
from datetimemixin.models import DateTimeMixin
from products.models import Product
import secrets


class ExtraFieldName(DateTimeMixin):
    name = models.CharField(
        max_length=255,
        blank=False,
        unique=True
    )
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(ExtraFieldName, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class ExtraFieldValue(DateTimeMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        related_name='extra_fields'
    )
    field_name = models.ForeignKey(
        ExtraFieldName,
        on_delete=models.CASCADE,
        blank=False,
        related_name="values"
    )
    value = models.CharField(
        max_length=255,
        blank=False,
    )
    sku = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('product', "field_name", "value",)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(ExtraFieldValue, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.field_name}={self.value}'



