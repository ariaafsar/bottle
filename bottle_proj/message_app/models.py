from django.db import models
from user_app.models import Account

class Conversation(models.Model):
    participants = models.ManyToManyField(Account)

class Message(models.Model):
    participant = models.ForeignKey(Conversation , on_delete=models.CASCADE)
    sender = models.ForeignKey(Account , on_delete=models.CASCADE)
    content = models.TextField()





# Create your models here.
