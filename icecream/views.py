from django.shortcuts import render
from .models import Icecream  # можно заменить на from .models import icecream_db

def icecreams_details(request, pk):
    name = Icecream.objects.get(id=pk)
    description = name.description
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-details.html', context)
