from config.urls import path
from catalog.views import index, contacts, CategoryListView, ProductListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', index, name='home'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/pruduct/', ProductListView.as_view(), name='product'),
    path('contacts/', contacts, name='contacts'),

]
