import secrets

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetimemixin.models import DateTimeMixin


class User(AbstractUser):
    """
    User class
    custom user model
    """
    role_choices = (
        ('cs', 'customer'),
        ('sl', 'seller'),
    )
    national_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    phone_number_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    role = models.CharField(
        max_length=2,
        blank=False,
        choices=role_choices,
        default='cs'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

class UserProfileImage(DateTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="images/users")
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        super(UserProfileImage, self).save(*args, **kwargs)
