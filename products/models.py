from django.db import models
from category.models import Category
import secrets


class ProductPack(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    # brand = models.ForeignKey()
    # shop = models.ForeignKey()
    image = models.ImageField(
        upload_to='images/products'
    )
    # comment = models.ManyToOneRel()
    sku = models.CharField(
        max_length=255,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(bytes=12)
        super(Product, self).save(*args, **kwargs)






