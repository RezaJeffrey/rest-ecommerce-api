from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='child', blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ('name', )





