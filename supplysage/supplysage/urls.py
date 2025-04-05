# supplysage/urls.py
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # Default Pages
    path('', RedirectView.as_view(url='/items/', permanent=False)),
    path('admin/', admin.site.urls),
    # Inventory Pages
    path('items/', include('inventory.urls')),
    # Authentication Pages
    path('accounts/', include('users.urls'), name="accounts"), # Include the custom authentication urls, put fisrst to avoid conflict with the default authentication urls
    path('accounts/', include('django.contrib.auth.urls'), name="accounts"), # Include the authentication urls 
]
