# supplysage/inventory/urls.py
from django.urls import path
from .views import (
    item_list_view,
    item_create_view,
    item_update_view,
    item_delete_view,
    export_inventory_csv,
    reports_view,
    export_low_stock_csv,
    export_low_stock_pdf,
)

urlpatterns = [
    path('', item_list_view, name='item_list'),
    path('create/', item_create_view, name='item_create'),
    path('update/<int:pk>/', item_update_view, name='item_update'),
    path('delete/<int:pk>/', item_delete_view, name='item_delete'),
    path('export/csv/', export_inventory_csv, name='export_inventory_csv'),
    path('reports/', reports_view, name='reports'),
    path('reports/export/csv/', export_low_stock_csv, name='export_low_stock_csv'),
    path('reports/export/pdf/', export_low_stock_pdf, name='export_low_stock_pdf'),
]
