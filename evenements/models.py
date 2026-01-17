from django.db import models
from membres.models import Membre


class Evenement(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lieu = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    participants = models.ManyToManyField(
        Membre, related_name='evenements', blank=True)

    def __str__(self):
        return self.titre
