from django.shortcuts import render
from anfis.models import Friend

# функция по добавлению данных в базу данных
def friends_registr(request):
    if request.method == 'POST':
        name_e = request.POST['name']
        city_e = request.POST['city']
        b = Friend(name=name_e, city=city_e)
        b.save()
    return render(request, 'friends_reg/friends.html')