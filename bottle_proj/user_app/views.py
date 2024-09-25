from django.shortcuts import render
from rest_framework import generics , status
from .models import Account
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.view import TokenObtainPairView , TokenRefreshView

class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

class Signup(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def Create(self , request , *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
