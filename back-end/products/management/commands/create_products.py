from django.core.management.base import BaseCommand, CommandError, CommandParser
from products.models import Product
from category.models import Category
from brands.models import Brand
from shops.models import Shop

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("number_of_products", type=int)
        return super().add_arguments(parser=parser)

    def handle(self, *args, **options) -> str | None:
        if (options["number_of_products"]):
            for i in range(options["number_of_products"]):
                category = Category.objects.get_or_create(name = f"category test {i + 1}")[0]
                brand = Brand.objects.get_or_create(name = f"brand test {i + 1}")[0]
                shop = Shop.objects.get_or_create(name = f"shop test {i + 1}", province = f"shop test {i + 1} province")[0]
                try:
                    product = Product(
                        name = f"product test {i + 1}",
                        category = category,
                        description = f"product description test {i + 1}",
                        brand = brand,
                    )
                    product.save()
                    product.shop.add(shop)
                except Exception as e:
                    self.stderr.write(f"could not create product test {i + 1} err: {e}!")
                    continue
        else:
            raise CommandError("number of profucts should be provided correctly!")