from rest_framework import serializers
from .models import Bottle

class ShopBottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = '__all__'

class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = ['id' , 'message']

class OwnedBottleSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(source='bought_bottle.price')
    range = serializers.IntegerField(source='bought_bottle.range')

    class Meta:
        model = Bottle
        fields = ['price', 'range']
