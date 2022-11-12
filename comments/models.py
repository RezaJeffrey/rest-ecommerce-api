from django.db import models
from datetimemixin.models import DateTimeMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from likes.models import Like
from django.contrib.auth import get_user_model
import secrets

User = get_user_model()


class Comment(DateTimeMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False
    )
    reply_comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='replies'
    )
    text = models.TextField(
        blank=False
    )
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    content_object = GenericForeignKey('content_type', 'object_id')
    likes = GenericRelation(Like, related_query_name='likes')
    sku = models.CharField(
        max_length=255,
        blank=False,
        unique=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"])
        ]

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = secrets.token_urlsafe(nbytes=12)
        return super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.content_object}, {self.user}, {self.text}"
