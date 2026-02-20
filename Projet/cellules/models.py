from django.db import models


class Cellule(models.Model):
    id_cellule = models.AutoField(primary_key=True)
    nom_cellule = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_cellule
