from config.urls import path
from catalog.views import product, category, index, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', index, name='home'),
    path('category/', category, name='category'),
    path('<int:pk>/pruduct/', product, name='product'),
    path('contacts/', contacts, name='contacts'),

]
