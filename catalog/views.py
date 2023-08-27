from django.shortcuts import render
from django.views.generic import ListView

from catalog.apps import CatalogConfig
from catalog.models import Product, Category

app_name = CatalogConfig


def index(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'
    extra_context = {
        'title': 'Категорий'
    }


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category.pk'] = category_item.pk

        return context_data
