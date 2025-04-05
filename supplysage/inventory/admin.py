# supplysage/inventory/admin.py
from django.contrib import admin
from .models import Item, InventorySettings

# Register your models here.
admin.site.register(Item)
admin.site.register(InventorySettings)