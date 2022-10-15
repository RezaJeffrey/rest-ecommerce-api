from django.db import models
from datetimemixin.models import DateTimeMixin
from django.contrib.auth import get_user_model
from products.models import Product


User = get_user_model()


class Cart(DateTimeMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="carts",
        blank=False
    )


