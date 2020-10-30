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
                    f' required value="{friend}">{friend} {friends_year[friend]}<br>')

    for i in range(len(icecream_db)):
        ice_form = (f'<input type="radio" name="icecream"'
                    f' required value="{icecream_db[i]["name"]}">{icecream_db[i]["name"]}')
        icelink = f"<a href='icecream/{i}/'>Узнать состав</a> <br>"
        icecreams += f'{ice_form} | {icelink} <br>'

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        city = friends_db[selected_friend]
        weather = what_weather(city)
        selected_icecream = request.POST['icecream']
        friend_output = f'{selected_friend}, тебе прислали {selected_icecream}!'
        city_weather = f'Погода в городе {city}: {weather}'


    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
    }

    return render(request, 'homepage/index.html', context)



