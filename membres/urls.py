from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mon-equipe/', views.mon_equipe, name='mon_equipe'),
]
