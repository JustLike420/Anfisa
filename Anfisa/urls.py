from django.contrib import admin
from django.urls import path
from homepage import views as home_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index),

]
