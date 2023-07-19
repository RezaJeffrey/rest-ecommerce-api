from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from carts.models import Cart
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def create_cart(sender, created, instance, **kwargs):
    if created:
        Cart.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_cart(sender, instance, **kwargs):
    instance.cart.save()
