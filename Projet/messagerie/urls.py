from django.urls import path
from . import views

urlpatterns = [
    path('', views.boite_reception, name='inbox'),
    path('composer/', views.envoyer_message, name='composer'),
]