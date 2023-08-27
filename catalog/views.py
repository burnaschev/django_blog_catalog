from django.shortcuts import render

from catalog.apps import CatalogConfig
from catalog.models import Product, Category

app_name = CatalogConfig


def index(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def category(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категорий',
    }
    return render(request, 'catalog/category.html', context)


def product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Продукт категорий {category_item.name_category}',
    }
    return render(request, 'catalog/product.html', context)
