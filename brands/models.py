from django.db import models
from datetimemixin.models import DateTimeMixin
import secrets


class Brand(DateTimeMixin):
    name = models.CharField(
        max_length=120,
        blank=False,
        unique=True
    )
    image = models.ImageField(
        upload_to='images/brand',
        blank=False
    )
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

