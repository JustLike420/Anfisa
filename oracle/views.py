from datetime import datetime
from django.shortcuts import render
from .services import zodiac, naz_goda, leap
# Create your views here.


def index(request):
    c = ''
    zod = ''
    naz_god = ''
    leaps = ''

    a = datetime.now()

    day, month, year = 30, 12, 2002
    if request.method == 'POST':

        date = request.POST['date']
        dates = date.split('-')
        year = int(dates[0])
        month = int(dates[1])
        day = int(dates[2])
        zod = zodiac(day, month)
        naz_god = naz_goda(year)
        leaps = leap(year)
        b = datetime(year, month, day)
        c = a - b
        c = c.days
    context = {
        'zod': zod,
        'naz_god': naz_god,
        'leaps': leaps,
        'days': c,
    }
    return render(request, 'oracle/oracle.html', context)