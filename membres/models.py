from django.db import models
from django.contrib.auth.models import User

class Cellule(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Profil(models.Model):
    POSTE_CHOICES = [
        ('CHEF', 'Chef de Cellule'),
        ('RESPONSABLE', 'Responsable'),
        ('MEMBRE', 'Membre Actif'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Lien avec l'utilisateur Django
    cellule = models.ForeignKey(Cellule, on_delete=models.SET_NULL, null=True, related_name='membres')
    poste = models.CharField(max_length=20, choices=POSTE_CHOICES, default='MEMBRE')
    telephone = models.CharField(max_length=20, blank=True)
    date_adhesion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.poste}"