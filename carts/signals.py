from django.db.models.signals import post_save
from carts.models import Cart, CartItem
from django.dispatch import receiver


@receiver(post_save, sender=CartItem)
def save_cart(sender, instance, **kwargs):
    instance.cart.save()
