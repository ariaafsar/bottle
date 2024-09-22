from django.shortcuts import render
from .models import Message , Conversation
from .serializers import MessageSerializer , ConversationSerializer
from rest_framework import generics

class ConversationsList(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
# Create your views here.
