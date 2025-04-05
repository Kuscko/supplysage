# supplysage/inventory/models.py
from django.db import models
from decimal import Decimal
from inventory.utils.emails import send_low_stock_email

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
    
    def get_total_value(self):
        return Decimal(self.quantity) * self.price
    
    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)
    
    def save(self, *args, **kwargs):
    # Check if this is an update
        if self.pk:
            old = Item.objects.get(pk=self.pk)
            threshold = InventorySettings.objects.first().low_stock_threshold

            dropped_below = old.quantity >= threshold and self.quantity < threshold

            notifications_enabled = InventorySettings.objects.first().low_stock_notifications_enabled
            if dropped_below and notifications_enabled:
                send_low_stock_email(self, threshold)  # Pass threshold as a parameter

        super().save(*args, **kwargs)

class InventorySettings(models.Model):
    low_stock_threshold = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"Low Stock Threshold: {self.low_stock_threshold}"

    class Meta:
        verbose_name_plural = "Inventory Settings"


