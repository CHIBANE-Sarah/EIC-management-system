from django.db import models


class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    contenu = models.TextField()
    type_message = models.CharField(max_length=50)
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    id_membre = models.ForeignKey(
        'membres.Membre', on_delete=models.CASCADE, related_name='messages_envoyes')
    id_membre_1 = models.ForeignKey(
        'membres.Membre', on_delete=models.CASCADE, related_name='messages_recus')

    def __str__(self):
        return f"Message {self.id_message}"
