import secrets
from django.db import models
from datetimemixin.models import DateTimeMixin
from django.contrib.auth import get_user_model
from discount.models import DiscountCode
from productpacks.models import ProductPack
from extra_fields.models import ExtraFieldValue, ExtraFieldName
from carts.validators import validate_none_zero
from django.utils import timezone

User = get_user_model()


class Cart(DateTimeMixin):
    user = models.OneToOneField(
        User,
        related_name='cart',
        on_delete=models.CASCADE
    )
    cart_total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        total = self.get_total_price()
        if total != self.cart_total_price:
            self.total_price = total
        return super(Cart, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}'s cart"

    def get_total_price(self):
        queryset = CartItem.objects.filter(cart__user=self.user)
        total = 0
        for item in queryset:
            total += item.get_item_total_price()
        return total


class CartItem(DateTimeMixin):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        blank=False,
        related_name='items'
    )
    item = models.ForeignKey(
        ProductPack,
        on_delete=models.CASCADE,
        blank=False,
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(
        blank=False,
        default=1,
        validators=[
            validate_none_zero
        ]
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_code = models.CharField(max_length=30, blank=True, null=True)
    sku = models.CharField(
        primary_key=True,
        max_length=255,
        blank=True,
        unique=True
    )

    class Meta:
        unique_together = ('cart', 'item')

    def __str__(self):
        return f'{self.item.product.name}'

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        # udpating total_price
        self.total_price = self.get_item_total_price()
        return super(CartItem, self).save(*args, **kwargs)

    def get_discount_code(self):
        query = DiscountCode.objects.filter(code=self.discount_code).first()
        if query:
            if timezone.now() < query.available_until or query.is_active:
                return query
            query.is_active = False
            query.save()
        else:
            return None

    def get_item_price_after_discount(self, *args, **kwargs):
        discount = self.get_discount_code()
        if discount:
            # updating discount amount after it's used
            if discount.amount:
                discount.amount -= 1
                discount.save()
            discounted_price = (discount.percent * self.item.price) / 100
            discount_limit = discount.discount_limit
            if discount_limit and (discounted_price > discount_limit):
                new_price = self.item.price - discount_limit
            else:
                new_price = self.item.price - discounted_price
        else:
            new_price = self.item.price
        return new_price

    def get_item_total_price(self):
        discount = self.get_discount_code()
        if discount:
            total_price = self.get_item_price_after_discount() * self.quantity
        else:
            total_price = self.item.price * self.quantity
        return total_price
