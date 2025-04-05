# supplysage/inventory/admin.py
from django.contrib import admin
from .models import Item, InventorySettings

class InventorySettingsAdmin(admin.ModelAdmin):
    list_display = ('low_stock_threshold', 'low_stock_notifications_enabled')

# Register your models here.
admin.site.register(Item)
admin.site.register(InventorySettings, InventorySettingsAdmin)