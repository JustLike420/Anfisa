import requests
# функция по нахождению погоды
def what_weather(city):
    url = f'http://wttr.in/{city}'  # погодный сервис + город выбраного друга
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'

# функция по нахождению кол-ва градусов
def what_temperature(weather):
    parsed_temperature = ''
    # если ошибка, выводим ошибку
    if (weather == '<сетевая ошибка>' or weather == '<ошибка на сервере погоды. попробуйте   позже>'):
        return weather

    temperature = weather.split()[1]  # цисловое значение температуры

    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char) # если симв цифра, пордолжить инчае ошибка
            parsed_temperature += char
        except ValueError:
            continue
        return parsed_temperature

# функция по определению мнения анфисы на кол-во градусов
def what_conclusion(parsed_temperature):
    try:
        temperature = int(parsed_temperature)
        if temperature < 18:
            return 'Мнение Анфисы: Холодно'
        elif (temperature >= 18 and temperature <= 27):
            return 'Мнение Анфисы: В самый раз'
        elif (temperature > 27):
            return 'Жарко'
    except ValueError:
        return 'Мнение Анфисы: Не могу узнать погоду'