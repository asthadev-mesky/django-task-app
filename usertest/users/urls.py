from django.urls import path
from .views import allUsers, loginUser, getCapacity

urlpatterns = [
    path('users/', allUsers, name='allUsers'),
    path('login/', loginUser, name='loginUser'),
    path('getCapacity/', getCapacity, name='getCapacity'),
    
]   

