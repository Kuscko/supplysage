# supplysage/inventory/urls.py
from django.urls import path
from .views import (
    item_list_view,
    item_create_view,
    item_update_view,
    item_delete_view,
    export_inventory_csv,
)

urlpatterns = [
    path('', item_list_view, name='item_list'),
    path('create/', item_create_view, name='item_create'),
    path('update/<int:pk>/', item_update_view, name='item_update'),
    path('delete/<int:pk>/', item_delete_view, name='item_delete'),
    path('export/csv/', export_inventory_csv, name='export_inventory_csv'),
]
