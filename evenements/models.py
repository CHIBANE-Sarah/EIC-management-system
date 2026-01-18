from django.db import models


class Evenement(models.Model):
    id_evenement = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    lieu = models.CharField(max_length=200)
    statut = models.CharField(max_length=50)

    participants = models.ManyToManyField(
        'membres.Membre', related_name='evenements_participes')

    def __str__(self):
        return self.titre
