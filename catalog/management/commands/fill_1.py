from django.core.management.commands import loaddata

from catalog.models import Category, Product


class Command(loaddata.Command):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        return super().handle(*args, **options)

