from django.db import models
from datetimemixin.models import DateTimeMixin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
import secrets
from django.core.validators import RegexValidator


class Address(DateTimeMixin):
    choices = (
        ('of', 'office'),
        ('hm', 'home'),
        ('fv', 'favorite'),
        ('nt', '------')
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='addresses', blank=True,
                             null=True)
    mode = models.CharField(max_length=2, choices=choices, blank=False, default='nt')
    name = models.CharField(max_length=64, blank=False)
    address = models.CharField(max_length=255, blank=False)
    post_code = models.CharField(
        max_length=10,
        verbose_name=_('postal code'),
        blank=False, unique=False,
        validators=[
            RegexValidator(
                r'^\d{1,10}$',
                message=_('only positive numbers alowed(10 digits)')
            )
        ]
    )
    sku = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(Address, self).save(*args, **kwargs)
