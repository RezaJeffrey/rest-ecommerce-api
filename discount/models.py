from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from datetimemixin.models import DateTimeMixin
from productpacks.models import ProductPack
from blacklists.models import Blacklist
import secrets


 # discount on single products using code/ discount by price
class DiscountCode(DateTimeMixin):
     code = models.CharField(max_length=30)
     available_untill = models.DateTimeField()


class ProductDiscount(DateTimeMixin):
     product_pack = models.ForeignKey(ProductPack, on_delete=models.CASCADE, related_name="product_discounts")
     discount_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, related_name="product_discounts")
     new_price = models.DecimalField(decimal_places=2, max_digits=14)
     percent = models.PositiveIntegerField(default=0)
     black_list = GenericRelation(Blacklist, related_query_name='discount')
     sku = models.CharField(max_length=255, blank=True, null=True)


     def save(self, *args, **kwargs):
         if not self.sku:
              self.sku = secrets.token_urlsafe(nbytes=12)
         return super(ProductDiscount, self).save(*args, **kwargs)

     def __str__(self):
         return f'{self.product_pack.product.name} -p {self.percent}%'
