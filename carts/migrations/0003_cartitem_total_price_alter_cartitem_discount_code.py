# Generated by Django 4.0.6 on 2022-12-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_total_price_cartitem_discount_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='discount_code',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
