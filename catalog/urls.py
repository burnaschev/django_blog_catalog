from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, index, contacts, CategoryListView, ProductCreateView, ProductUpdateView, \
    ProductDetailView, ProductDeleteView
from config.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('pruduct/<int:pk>', ProductListView.as_view(), name='product_list'),
    path('product/view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('product/create/',  never_cache(ProductCreateView.as_view()), name='product_create'),
    path('<int:pk>/product/edit/',  never_cache(ProductUpdateView.as_view()), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]
