from django.db import models
from membres.models import Profil

class Evenement(models.Model):
    CATEGORIE_CHOICES = [
        ('REUNION', 'Réunion'),
        ('FORMATION', 'Formation'),
        ('EVENEMENT', 'Événement'),
        ('AUTRE', 'Autre'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default='EVENEMENT')
    createur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='evenements_crees')
    participants = models.ManyToManyField(Profil, related_name='evenements_participe', blank=True)

    def __get_color(self):
        # Couleurs basées sur le PDF (Page 7/8)
        colors = {
            'REUNION': '#0d6efd',   # Bleu
            'FORMATION': '#198754', # Vert
            'EVENEMENT': '#ffc107', # Jaune
            'AUTRE': '#6c757d',     # Gris
        }
        return colors.get(self.categorie, '#0d6efd')

    def __str__(self):
        return self.titre