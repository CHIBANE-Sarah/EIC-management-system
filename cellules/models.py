from django.db import models


class Cellule(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_cellule
