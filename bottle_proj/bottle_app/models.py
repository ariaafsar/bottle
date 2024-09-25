from django.db import models
from user_app.models import Account

class ShopBottle(models.Model):
    price = models.IntegerField()
    bottle_range = models.IntegerField()
    content_legth = models.IntegerField()

    def __str__(self):
        return {(self.price) - (self.bottle_range) - (self.content_legth)}
    
class Bottle(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE , related_name='sender')
    reciver = models.ForeignKey(Account, on_delete=models.CASCADE , related_name='reciver')
    content = models.TextField()
    date_and_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.user.username
# Create your models here.
