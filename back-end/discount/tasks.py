from celery import shared_task
from discount.models import DiscountCode
from datetime import datetime


@shared_task()
def expiring_expired_product_discount_code(*args, **kwargs):
    objects = DiscountCode.objects.filter(available_untill__lte = datetime.now()).prefetch_related("product_discounts")
    for object in objects:
        product_discounts = object.product_discounts.filter(black_list=None)
        for product_discount in product_discounts:
            product_discount.black_list.create(
                name="product_discount_blacklist"
            )
    