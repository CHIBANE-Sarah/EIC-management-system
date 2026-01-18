from django.db import models


class Contact(models.Model):
    id_contact = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=200, blank=True)
    type_contact = models.CharField(max_length=50)
    remarque = models.CharField(max_length=100, blank=True)

    id_membre = models.ForeignKey('membres.Membre', on_delete=models.CASCADE)
    id_cellule = models.ForeignKey(
        'cellules.Cellule', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
