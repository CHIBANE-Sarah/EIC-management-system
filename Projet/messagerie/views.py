from django.shortcuts import render, redirect
from .models import Message
from membres.models import Profil

def boite_reception(request):
    try:
        mon_profil = Profil.objects.get(user=request.user)
    except Profil.DoesNotExist:
        return redirect('dashboard')
    messages_recus = Message.objects.filter(destinataire=mon_profil).order_by('-date_envoi')
    
    return render(request, 'messagerie/inbox.html', {'messages': messages_recus})

def envoyer_message(request):
    profils = Profil.objects.exclude(user=request.user) # On peut écrire à tout le monde sauf soi-même
    
    if request.method == 'POST':
        destinataire_id = request.POST.get('destinataire')
        objet = request.POST.get('objet')
        contenu = request.POST.get('contenu')
        
        destinataire = Profil.objects.get(id=destinataire_id)
        
        Message.objects.create(
            expediteur=request.user.profil,
            destinataire=destinataire,
            objet=objet,
            contenu=contenu
        )
        return redirect('inbox')
        
    return render(request, 'messagerie/composer.html', {'profils': profils})