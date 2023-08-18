from django.core import management
from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        management.call_command('loaddata', 'catalog_data.json', verbosity=0,)
