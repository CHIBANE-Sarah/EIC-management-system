from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        nom_utilisateur = request.POST.get('username')
        mot_de_passe = request.POST.get('password')

        user = authenticate(username=nom_utilisateur, password=mot_de_passe)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Identifiants invalides")

    return render(request, 'authentification/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
