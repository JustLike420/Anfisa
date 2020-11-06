from django.shortcuts import render
from .models import Icecream
from Anfisa.settings import STATIC_URL

# функция по выводу страницы с мороженым
def icecreams_details(request, pk):
    name = Icecream.objects.get(id=pk)  # quaryset по выбраному мороженому
    description = name.description  # описание мороженого
    img = name.img  # изображение мороженого
    context = {
        'name': name,  # название
        'description': description,  # описание
        'pk': pk,  # primary_key
        'image': img,  # изображение
    }
    return render(request, 'icecream/icecream-details.html', context)
