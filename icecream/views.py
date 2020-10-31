from django.shortcuts import render
from .models import Icecream  # можно заменить на from .models import icecream_db
from Anfisa.settings import STATIC_URL

def icecreams_details(request, pk):
    name = Icecream.objects.get(id=pk)
    description = name.description

    context = {
        'name': name,
        'description': description,
        'pk': pk,
        'STATIC_URL': STATIC_URL,
    }
    return render(request, 'icecream/icecream-details.html', context)
