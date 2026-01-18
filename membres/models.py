from django.db import models


class Membre(models.Model):
    id_membre = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=50)
    statut = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    id_cellule = models.ForeignKey(
        'cellules.Cellule', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
