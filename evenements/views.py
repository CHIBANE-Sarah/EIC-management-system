from django.shortcuts import render
from django.http import JsonResponse
from .models import Evenement

def calendrier_view(request):
    return render(request, 'evenements/calendrier.html')

def evenements_json(request):
    # Cette vue renvoie les données pour FullCalendar
    events = Evenement.objects.all()
    data = []
    for event in events:
        data.append({
            'title': event.titre,
            'start': event.date_debut.isoformat(),
            'end': event.date_fin.isoformat(),
            'color': event.__get_color(), # On utilise notre logique de couleur
        })
    return JsonResponse(data, safe=False)