# supplysage/inventory/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Item, InventorySettings
from django.contrib.auth.models import User

# Create your tests here.
class InventorySearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        Item.objects.create(name='Laptop', quantity=5, price=999.99, category='ELECTRONICS')
        Item.objects.create(name='Desk', quantity=2, price=150.00, category='FURNITURE')

    def test_search_items(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.get(reverse('item_list'), {'q': 'laptop'})
        self.assertContains(response, 'Laptop')
        self.assertNotContains(response, 'Desk')

    def test_filter_by_category(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.get(reverse('item_list'), {'category': 'FURNITURE'})
        self.assertContains(response, 'Desk')
        self.assertNotContains(response, 'Laptop')

class LowStockTests(TestCase):
    def setUp(self):
        InventorySettings.objects.create(low_stock_threshold=10)

    def test_item_low_stock_flag(self):
        item = Item.objects.create(name='Widget', quantity=5, price=20.00, category='OTHER')
        self.assertTrue(item.is_low_stock())

        item.quantity = 15
        item.save()
        self.assertFalse(item.is_low_stock())
        
    def test_item_quantity_equal_to_threshold(self):
        item = Item.objects.create(name='Widget', quantity=10, price=20.00, category='OTHER')
        self.assertFalse(item.is_low_stock())