from django.contrib.admin import register , ModelAdmin
from .models import Bottle , ShopBottle

@register(Bottle)
class BottleAdmin(ModelAdmin):
    pass

@register(ShopBottle)
class ShopBottleAdmin(ModelAdmin):
    pass

# Register your models here.
