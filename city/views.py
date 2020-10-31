from django.shortcuts import render
from .models import Citys
# Create your views here.
def GetCity(requset):
    city = Citys.objects.all()
    return render(requset, 'city/city-list.html', {'city': city})