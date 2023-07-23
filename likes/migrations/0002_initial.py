# Generated by Django 4.0.6 on 2023-07-23 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('likes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='like',
            index=models.Index(fields=['content_type', 'object_id'], name='likes_like_content_5c134b_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'object_id')},
        ),
    ]