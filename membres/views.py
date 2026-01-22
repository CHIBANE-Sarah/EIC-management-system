from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    context = {
        'segment': 'dashboard',
    }
    return render(request, 'membres/dashboard.html', context)
