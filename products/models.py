from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from category.models import Category
from datetimemixin.models import DateTimeMixin
from django.contrib.auth import get_user_model
from likes.models import Like
from comments.models import Comment
import secrets

User = get_user_model()


class ShopAddress(DateTimeMixin):
    address = models.CharField(max_length=500)
    postal_code = models.PositiveBigIntegerField(blank=True, null=True)  # TODO postal code iran format(max, min length)

    def __str__(self):
        return self.address[:35]


class Shop(DateTimeMixin):
    name = models.CharField(max_length=255)
    province = models.CharField(max_length=120)  # TODO choicefields for province
    address = models.OneToOneField(ShopAddress, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Brand(DateTimeMixin):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/brand')

    def __str__(self):
        return self.name


class Product(DateTimeMixin):
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
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )
    likes = GenericRelation(Like, related_query_name='likes')
    comments = GenericRelation(Comment, related_query_name='comments')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        super(Product, self).save(*args, **kwargs)


class ProductImage(DateTimeMixin):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products')
    alt_text = models.CharField(max_length=255, blank=True, null=True)


class ExtraFieldName(DateTimeMixin):
    name = models.CharField(
        max_length=255,
        blank=False,
        unique=True
    )

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


