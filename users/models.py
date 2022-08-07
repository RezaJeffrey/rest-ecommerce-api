from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    User class
    custom user model
    """
    national_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    phone_number_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
