from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model
from eav.decorators import register_eav
import secrets

User = get_user_model()


class DateTimeMixin(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Shop(DateTimeMixin):
    name = models.CharField(max_length=255)
    province = models.CharField(max_length=120)  # TODO choicefields for province
    # TODO address model
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class ProductPack(DateTimeMixin):
#     pass


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


class Comment(DateTimeMixin):
    # TODO like/reply model
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=1200)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
