from django.db import models
from datetimemixin.models import DateTimeMixin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from carts.models import Cart
from address.models import Address
import secrets


class Order(DateTimeMixin):
    PAYMENT_METHOD_CHOICE = (
        ('cd', 'cash on delivery'),
        ('nb', 'net banking'),
        ('cp', 'card payment'),
        ('wl', 'wallet')
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=False,
        related_name='orders'
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        blank=False,
        related_name='orders'
    )
    order_cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        related_name='order'
    )
    payment_method = models.CharField(
        max_length=2,
        choices=PAYMENT_METHOD_CHOICE,
        blank=False,
        default='cd',
        verbose_name=_('payment method')
    )
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}'s order"


class OrderStatus(DateTimeMixin):
    STATUS_CHOICE = (
        ('pn', 'order pending'),
        ('oa', 'order approved'),
        ('sp', 'order shipped'),
        ('od', 'order delivered'),
        ('oc', 'order cancelled'),
        ('or', 'order returned')
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICE,
        blank=False,
        default='pn'
    )
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='status'
    )
    sku = models.CharField(
        max_length=255,
        blank=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(OrderAdmin, self).save(*args, **kwargs)

    def __str__(self):
        return self.status

