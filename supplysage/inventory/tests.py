# supplysage/inventory/tests.py
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from decimal import Decimal
from .models import Item, InventorySettings

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

class InventoryValueTests(TestCase):
    def test_total_value_calculation(self):
        item = Item.objects.create(name='Chair', quantity=3, price=49.99, category='FURNITURE')
        self.assertEqual(item.get_total_value(), 149.97)

class LowStockEmailTests(TestCase):
    def setUp(self):
        InventorySettings.objects.create(low_stock_threshold=10, low_stock_notifications_enabled=True)
        self.item = Item.objects.create(name='Widget', quantity=15, price=Decimal('5.00'), category='OTHER')

    @patch('inventory.utils.send_low_stock_email')
    def test_email_sent_when_dropping_below_threshold(self, mock_send_mail):
        self.item.quantity = 5
        self.item.save()
        self.assertTrue(mock_send_mail.called)
        self.assertIn('Low Stock Alert', mock_send_mail.call_args[0][0])  # subject check

    @patch('inventory.utils.send_low_stock_email')
    def test_no_email_if_not_below_threshold(self, mock_send_mail):
        self.item.quantity = 11
        self.item.save()
        self.assertFalse(mock_send_mail.called)

    @patch('inventory.utils.send_low_stock_email')
    def test_no_email_if_notifications_disabled(self, mock_send_mail):
        settings = InventorySettings.objects.first()
        settings.low_stock_notifications_enabled = False
        settings.save()

        self.item.quantity = 5
        self.item.save()
        self.assertFalse(mock_send_mail.called)

