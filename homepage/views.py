from django.shortcuts import render
from icecream.models import icecream_db
from anfis.models import friends_db
from anfis.services import what_weather

def index(request):
    icecreams = ''
    friends = ''
    city_weather = ''
    friend_output = ''

    for friend in friends_db:
        friends += (f'<input type="radio" name="friend"'
                    f' required value="{friend}">{friend}<br>')

    for i in range(len(icecream_db)):
        icecreams += f"{icecream_db[i]['name']} | <a href='icecream/{i}/'>Узнать состав</a> <br>"

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        city = friends_db[selected_friend]
        weather = what_weather(city)
        friend_output = f'{selected_friend}, тебе прислали мороженое!'
        city_weather = f'Погода в городе {city}: {weather}'

    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
    }

    return render(request, 'homepage/index.html', context)



