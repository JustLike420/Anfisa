from django.shortcuts import render
from anfis.services import what_weather, what_temperature, what_conclusion
from anfis.models import Friend
from icecream.models import Icecream

def index(request):
    icecreams = ''
    friends = ''
    city_weather = ''
    friend_output = ''
    parsed_temperature = ''
    conclusion = ''
    friend_database = Friend.objects.all()
    icecream_database = Icecream.objects.all()
    i = 1

    for friend in friend_database:
        friends += (f'<input type="radio" name="friend"'
                    f' required value="{friend}">{friend}<br>')

    for cream in icecream_database:
        ice_form = (f'<input type="radio" name="icecream"'
                    f' required value="{cream}">{cream}')
        icelink = f"<a href='icecream/{i}/'>Узнать состав</a> <br>"
        icecreams += f'{ice_form} | {icelink}'
        i += 1

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        k = Friend.objects.get(name=selected_friend)
        city = k.city
        weather = what_weather(city)
        selected_icecream = request.POST['icecream']
        parsed_temperature = what_temperature(weather)
        conclusion = what_conclusion(parsed_temperature)
        friend_output = f'{selected_friend}, тебе прислали {selected_icecream}!'
        city_weather = f'Погода в городе {city}: {weather}'


    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
        'parsed_temperature': parsed_temperature,
        'conclusion': conclusion,
    }

    return render(request, 'homepage/index.html', context)



