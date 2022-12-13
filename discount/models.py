from django.db import models
from datetimemixin.models import DateTimeMixin
from products.models import Product


# discount on single products using code/ discount by price
class DiscountCode(DateTimeMixin):
    code = models.CharField(max_length=30)
    available_untill = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class ProductDiscount(DateTimeMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE)
    new_price = models.DecimalField(decimal_places=2)
    percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} -p {self.percent}%'
