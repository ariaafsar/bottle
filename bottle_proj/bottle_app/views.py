from django.shortcuts import render
from .models import Bottle , ShopBottle
from .serializers import BottleSerializer , ShopBottleSerializer 
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *

class SendBottle(generics.CreateAPIView):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
    def create(self , request , *args , **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            sender = request.user.account
            reciver = serializer.validated_data['reciver']
            if not reciver.valid():
                Response({'user does not exist'} , status=status.http_400_bad_request)
            message =  serializer.validated_data['content']
            bottle_list = Bottle.objects.create(sender = sender , reciver = reciver , content = message)
            if not bottle.valid():
                Response({'you dont have chosen bottle'} , status=status.http_400_bad_request)
            bottle = bottle_list[0]
            if not bottle.valid():
                Response()

class BottleShopList(generics.listAPIView):
    queryset = ShopBottle.objects.all()
    serializer_class = BottleSerializer
    permission_classes = [IsAuthenticated]

class BuyBottle(generics.CreateAPIView):
    queryset = Bottle.objects.all()
    serializer_class = ShopBottleSerializer
    permission_classes = [IsAuthenticated]

    def create(self , request , *args , **kwargs):
        bought_bottle = self.request.data.get('bought_bottle')
        if not bought_bottle:
            raise serializers.ValidationError({'error': 'bought_bottle is required'})

        sender = self.request.user.account
        bottle_instance = ShopBottle.objects.get(id=bought_bottle)
        
        if sender.score < bottle_instance.price:
            raise serializers.ValidationError({'message': 'You don’t have enough score to buy this bottle'})

        sender.score -= bottle_instance.price
        sender.save()
        serializers.save(sender=self.request.user.account , bought_bottle=bottle_instance)





# Create your views here.
