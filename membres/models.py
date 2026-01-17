from django.db import models
from cellules.models import Cellule


class Membre(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=50)
    statut = models.CharField(max_length=50)

    ROLE_CHOICES = [
        ('Membre', 'Membre'),
        ('ADMIN', 'Admin'),
        ('RH', 'RH'),
        ('CHEF', 'Chef de cellule'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    cellule = models.ForeignKey(
        Cellule, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
