# supplysage/views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html') # Render the home page