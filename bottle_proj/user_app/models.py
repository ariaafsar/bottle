from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='user')
    bcoin = models.IntegerField(default=100)
    x = models.IntegerField()
    y = models.IntegerField()
    max_daily_bottle = models.IntegerField(default=3)
    reply_able = models.BooleanField(default=False)
    read_bottles = models.IntegerField(default=0)
    

# Create your models here.
