from django.contrib import admin
from anfis.models import Friend
from icecream.models import Icecream

# подключение БД в админку
admin.site.register(Friend)
admin.site.register(Icecream)
