from django.shortcuts import render
from . import models  # можно заменить на from .models import icecream_db


def icecream_list(request):
    db_query = models.icecream_db # получаем данные: полный список сортов
    icecreams = ''
    for i in range(len(db_query)):
        icecreams += f'<a href="{i}/">{db_query[i]["name"]}</a><br>'
    context = {'icecreams': icecreams}

    return render(request, 'icecream/icecream-list.html', context)

def icecreams_details(request, pk):
    name = models.icecream_db[pk]['name']
    description = models.icecream_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-details.html', context)
