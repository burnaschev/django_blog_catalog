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
    path('product/view/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/product/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]
