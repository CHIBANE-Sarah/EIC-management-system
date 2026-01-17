from django.db import models
from membres.models import Membre


class Message(models.Model):
    contenu = models.TextField()
    type_message = models.CharField(max_length=50)
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    expediteur = models.ForeignKey(
        Membre, on_delete=models.CASCADE, related_name='messages_envoyes')

    destinataire = models.ForeignKey(
        Membre, on_delete=models.CASCADE, related_name='messages_recus')

    def __str__(self):
        return f"Message de {self.expediteur}"
