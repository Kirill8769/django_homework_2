from django.urls import path

from catalog import apps, views

app_name = apps.CatalogConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts"),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product_create/', views.product_create, name='product_create'),
]
