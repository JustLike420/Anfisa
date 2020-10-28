from django.shortcuts import render
from . import models  # можно заменить на from .models import icecream_db


def icecream_list(request):
    db_query = models.icecream_db # получаем данные: полный список сортов
    icecreams = ''
    for i in range(len(db_query)):
        icecreams += f'{db_query[i]["name"]}'
    ice = {'icecream': icecreams}

    return render(request, 'icecream/icecream-list.html', context=ice)