from django.shortcuts import render
from anfis.services import what_weather, what_temperature, what_conclusion
from anfis.models import Friend
from icecream.models import Icecream

# главная функция
def index(request):

    # обязательно делаем пустые строки
    icecreams = ''
    friends = ''
    city_weather = ''
    friend_output = ''
    parsed_temperature = ''
    conclusion = ''

    # quaryset
    friend_database = Friend.objects.all()
    icecream_database = Icecream.objects.all()


    # список друзей с радио кнопкой
    for friend in friend_database:
        friends += (f'<input type="radio" name="friend"'
                    f' required value="{friend}">{friend}<br>')

    # список мороженого с радио кнопкой
    for cream in icecream_database:
        ice_form = (f'<input type="radio" name="icecream"'
                    f' required value="{cream}">{cream}')
        icecreams += f'{ice_form} <br>'

    # если есть запрос от пользователя
    if request.method == 'POST':
        selected_friend = request.POST['friend']  # выбраный друг помещается в переменную
        k = Friend.objects.get(name=selected_friend)  # quaryset выбраного друга
        city = k.city  # город друга
        weather = what_weather(city)  # погода в городе друга
        parsed_temperature = what_temperature(weather)  # кол-во градусов в городе выбраного друга
        conclusion = what_conclusion(parsed_temperature)  # мнение анфисы о погоде
        selected_icecream = request.POST['icecream']  # выбраное мороженое
        ice = Icecream.objects.get(name=selected_icecream)  # quaryset выбраного мороженого
        # Артем, тебе прислали фруктовое мороженое | Узнать состав(сылка на страницу с мороженым)
        friend_output = f'{selected_friend}, тебе прислали {selected_icecream} |' \
                        f' <a href="icecream/{ice.id}/">Узнать состав</a> <br>'
        city_weather = f'Погода в городе {city}: {weather}'  # погода в городе Москва: ☀️ 🌡️+14°C 🌬️↗0.0m/s

    context = {
        'icecreams': icecreams,  # список мороженого
        'friends': friends,  # список друзей
        'friend_output': friend_output,  # Артем, тебе прислали...
        'city_weather': city_weather,  # погода в городе Москва: ☀️ 🌡️+14°C 🌬️↗0.0m/s
        'conclusion': conclusion,  # мнение Анфисы
    }

    return render(request, 'homepage/index.html', context)




