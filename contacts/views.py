from django.shortcuts import render
from .models import Contact

def liste_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/liste_contacts.html', {'contacts': contacts})