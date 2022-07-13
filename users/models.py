from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    national_code = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone_number_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

