# Generated by Django 4.0.6 on 2022-12-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productpacks', '0005_alter_productpack_extra_field_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpack',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='productpack',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
