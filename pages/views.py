from django.shortcuts import render
from .models import Item

def home_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home.html', context)

