from django.shortcuts import render
from .models import Icecream  # можно заменить на from .models import icecream_db


def icecream_list(request):
    db_query = Icecream # получаем данные: полный список сортов
    icecreams = ''
    i = 1
    for cream in db_query:
        icecreams += f'<a href="{i}/">{cream}</a><br>'
    context = {'icecreams': icecreams}
    return render(request, 'icecream/icecream-list.html', context)

def icecreams_details(request, pk):
    name = Icecream.objects.get(id=pk)
    description = name.description
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-details.html', context)
