from django.shortcuts import render
from django.http import HttpResponse
from . import models  # можно заменить на from .models import icecream_db

def icecream_list(request):
    db_query = models.icecream_db # получаем данные: полный список сортов
    icecream = ''
    for i in range(len(db_query)):
        icecream += f'{db_query[i]["name"]} :: '
    icecreams = f'Список мороженного: {icecream}'
    return HttpResponse(icecreams)