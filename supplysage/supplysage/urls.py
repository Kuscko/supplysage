# supplysage/urls.py
from django.contrib import admin
from django.urls import include, path
from .views import home_view

urlpatterns = [
    # Default Pages
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    # Inventory Pages
    path('items/', include('inventory.urls')),
    # Authentication Pages
    path('accounts/', include('users.urls'), name="accounts"), # Include the custom authentication urls, put fisrst to avoid conflict with the default authentication urls
    path('accounts/', include('django.contrib.auth.urls'), name="accounts"), # Include the authentication urls 
]
