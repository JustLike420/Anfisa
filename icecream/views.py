from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def icecream_list(request):
    return HttpResponse('Здесь будет список морожеглшл')