from django.db import models

class Contact(models.Model):
    TYPE_CHOICES = [
        ('ENTREPRISE', 'Entreprise'),
        ('PARTENAIRE', 'Partenaire'),
        ('INTERVENANT', 'Intervenant'),
    ]

    nom = models.CharField(max_length=100)
    type_contact = models.CharField(max_length=20, choices=TYPE_CHOICES)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    derniere_interaction = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.nom} ({self.type_contact})"