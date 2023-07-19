from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from datetimemixin.models import DateTimeMixin
from django.conf import settings
import secrets


User = settings.AUTH_USER_MODEL


class Like(DateTimeMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    sku = models.CharField(
        max_length=255,
        blank=False,
        unique=False
    )

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"])
        ]
        unique_together = ('user', 'object_id')

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(Like, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

