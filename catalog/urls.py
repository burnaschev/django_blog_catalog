from config.urls import path
from catalog.views import ProductListView, index, contacts, CategoryListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/pruduct/', ProductListView.as_view(), name='product'),
]
