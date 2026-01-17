from django.db import models
from membres.models import Membre
from cellules.models import Cellule


class Contact(models.Model):
    nom = models.CharField(max_length=50)
    poste = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    likendin = models.URLField(blank=True, null=True)
    remarque = models.CharField(max_length=100, blank=True)

    membre = models.ForeignKey(
        Membre, on_delete=models.CASCADE, related_name='contacts')
    cellule = models.ForeignKey(
        Cellule, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.nom
