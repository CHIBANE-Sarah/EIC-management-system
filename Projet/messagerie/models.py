from django.db import models
from membres.models import Profil

class Message(models.Model):
    expediteur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='envoyes')
    destinataire = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='recus')
    objet = models.CharField(max_length=200)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"De {self.expediteur} à {self.destinataire} : {self.objet}"