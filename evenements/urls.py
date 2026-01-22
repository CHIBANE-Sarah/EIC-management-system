from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendrier_view, name='calendrier'),
    path('api/events/', views.evenements_json, name='evenements_json'),
]