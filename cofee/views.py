from django.shortcuts import render
from .models import cofee  # Corrected model name to Coffee

def home(request):
    cofees = cofee.objects.all()  # Corrected model name to Coffee and added parentheses to .all()
    return render(request, 'home.html', {
        'cofees': cofees  # Corrected variable name to items
    })
