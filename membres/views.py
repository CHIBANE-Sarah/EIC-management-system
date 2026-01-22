from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    context = {
        'segment': 'dashboard',
    }
    return render(request, 'membres/dashboard.html', context)

from django.shortcuts import render
from .models import Profil

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profil

def mon_equipe(request):
    try:
        mon_profil = Profil.objects.get(user=request.user)
        
        if not mon_profil.cellule:
            return render(request, 'membres/equipe.html', {'error': "Vous n'êtes affecté à aucune cellule."})

        equipe = Profil.objects.filter(cellule=mon_profil.cellule)
        return render(request, 'membres/equipe.html', {
            'equipe': equipe,
            'ma_cellule': mon_profil.cellule
        })
        
    except Profil.DoesNotExist:
        messages.warning(request, "Votre profil n'est pas encore configuré.")
        return redirect('dashboard')
