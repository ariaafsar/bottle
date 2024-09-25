from django.urls import path 
from .views import SendBottle , BottleShopList , BuyBottle

urlpatterns = [
    path('sendbottle' , SendBottle.as_view()),
    path('bottleshoplist' , BottleShopList.as_view()),
    path('buybottle' , BuyBottle.as_view())
]
