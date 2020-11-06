from django.shortcuts import render
from icecream.models import Icecream

# функция по добавлению данных в базу данных
def icecream_registr(request):
    if request.method == 'POST':
        icecream = request.POST['name']
        description = request.POST['description']
        b = Icecream(name=icecream, description=description)
        b.save()
    return render(request, 'icecream_reg/icecream.html')