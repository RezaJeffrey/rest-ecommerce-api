from products.models import ExtraFields, DateTimeMixin
from django.db import models


class ProductPack(DateTimeMixin):
    field = models.ForeignKey(
        ExtraFields,
        on_delete=models.CASCADE,
        related_name='packs'
    )
    value = models.CharField(
        max_length=255,
        blank=False,
    )



