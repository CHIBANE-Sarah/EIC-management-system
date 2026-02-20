from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentification.urls')),
    path('', include('membres.urls')),
    path('contacts/', include('contacts.urls')),
    path('calendrier/', include('evenements.urls')),
    path('messages/', include('messagerie.urls')),
]
