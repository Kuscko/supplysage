# supplysage/inventory/utils/emails.py
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def send_low_stock_email(item):
    # Lazy load the settings to avoid circular imports
    from inventory.models import InventorySettings
    User = get_user_model()

    # Get the low stock threshold from settings
    subject = f"Low Stock Alert: {item.name}"
    message = f"The item '{item.name}' has dropped below the stock threshold.\n\n" \
              f"Quantity: {item.quantity}\nThreshold: {InventorySettings.objects.first().low_stock_threshold}"
    from_email = settings.DEFAULT_FROM_EMAIL

    recipient_list = list(
        User.objects.filter(is_active=True)
        .filter(models.Q(is_staff=True) | models.Q(is_superuser=True))
        .exclude(email='')
        .values_list('email', flat=True)
    )

    send_mail(subject, message, from_email, recipient_list)
