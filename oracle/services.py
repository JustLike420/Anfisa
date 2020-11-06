def zodiac(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    if (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    if (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Блихнецы"
    if (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    if (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    if (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    if (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"


def naz_goda(year):
    god = ["Год обезьяны", "Год петуха", "Год собаки", "Год свиньи", "Год крысы", "Год быка",
           "Год тигра", "Год кролика", "Год дракона", "Год змеи", "Год лошади", "Год козы"]
    naz = god[year % 12]
    return naz


def leap(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return "Это високосный год"
    else:
        return "Это не високосный год"
