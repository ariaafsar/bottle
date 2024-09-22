from django.urls import path 
from .views import ConversationsList

urlpatterns = [
    path('list' , ConversationsList.as_view() , name='conversation_list') , 
]