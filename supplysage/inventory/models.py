# supplysage/inventory/models.py
from django.db import models

# Create your models here.
class Item(models.Model):
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Electronics'),
        ('FURNITURE', 'Furniture'),
        ('CLOTHING', 'Clothing'),
        ('FOOD', 'Food'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='OTHER')

    def __str__(self):
        return f'{self.name} - (Qty: {self.quantity})'
    
    @staticmethod
    def get_threshold():
        settings = InventorySettings.objects.get_or_create()[0]
        return settings.low_stock_threshold if settings else 5  # default fallback
    
    def is_low_stock(self):
        return self.quantity < Item.get_threshold()

    
class InventorySettings(models.Model):
    low_stock_threshold = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"Low Stock Threshold: {self.low_stock_threshold}"

    class Meta:
        verbose_name_plural = "Inventory Settings"


