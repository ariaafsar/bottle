from django.contrib.admin import register , ModelAdmin
from .models import Account

@register(Account)
class AccountAdmin(ModelAdmin):
    pass
# Register your models here.
