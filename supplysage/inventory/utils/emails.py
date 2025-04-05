# supplysage/inventory/utils/emails.py
from django.core.mail import send_mail
from django.conf import settings

def send_low_stock_email(item):
    # Lazy load the settings to avoid circular imports
    from inventory.models import InventorySettings
    # Get the low stock threshold from settings
    subject = f"Low Stock Alert: {item.name}"
    message = f"The item '{item.name}' has dropped below the stock threshold.\n\n" \
              f"Quantity: {item.quantity}\nThreshold: {InventorySettings.objects.first().low_stock_threshold}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [admin[1] for admin in settings.ADMINS]  # or a static list like ['store@example.com']
    
    send_mail(subject, message, from_email, recipient_list)
