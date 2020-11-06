from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('icecream/', include('icecream.urls')),
    path('friends/', include('friends_reg.urls')),
    path('icecreams/', include('icecream_reg.urls')),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)