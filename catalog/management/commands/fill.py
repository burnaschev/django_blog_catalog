
from django.core.management import BaseCommand
from django.utils.datetime_safe import datetime

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [{'name': 'iPhone12 ', 'description': 'Новый',
                         'product_category': 'Смартфоны',
                         'product_price': 12_000, 'create_date': None},
                        {'product_name': 'Hp', 'product_description': 'Ультра тонкий',
                         'product_category': 'Ноутбуки',
                         'product_price': 6_0000, 'create_date': None},
                        {'product_name': 'Наушники JBL', 'product_description': 'Хорошее звучание',
                         'product_category': 'Аксессуары',
                         'product_price': 3200, 'create_date': datetime.now()},
                        {'product_name': 'Samsung', 'product_description': 'Огромный',
                         'product_category': 'Телевизоры',
                         'product_price': 67_000, 'create_date': datetime.now()},
                        ]
        products_for_create = []
        Product.objects.all().delete()
        for product in product_list:
            products_for_create.append(Product(**product))

        Product.object.create(products_for_create)
