from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from .models import Account
class Register(CreateAPIView):
    pass
# Create your views here.
