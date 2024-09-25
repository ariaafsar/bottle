from django.urls import path 
from .views import Signup , Login , Refresh

urlpatterns = [
    path('Signup'  , Signup.as_view()),
    path('Login' , Login.as_view()),
    path('Refresh' , Refresh.as_view()),
]
