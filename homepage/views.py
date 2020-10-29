from django.shortcuts import render
from icecream.models import icecream_db
from anfis.models import friends_db
from anfis.services import what_weather

def index(request):
    icecreams = ''
    friends = ''
    for friend in friends_db:
        city = friends_db[friend]
        weather = what_weather(city)
        friends += f'{friend} :: {city} :: {weather} <br>'

    for i in range(len(icecream_db)):
        icecreams += f"{icecream_db[i]['name']} | <a href='icecream/{i}/'>Узнать состав</a> <br>"

    context = {
        'icecreams': icecreams,
        'friends': friends,
    }

    return render(request, 'homepage/index.html', context)



