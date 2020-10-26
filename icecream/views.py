from django.shortcuts import render
from django.http import HttpResponse
from . import models

def icecream_list(request):
    db_query = models.icecream_db # получаем данные: полный список сортов
    icecreams = f'Список мороженного {db_query}'
    return HttpResponse(icecreams)