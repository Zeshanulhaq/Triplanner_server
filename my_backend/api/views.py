from django.shortcuts import render
from .models import Booking, Pakg, User
from .serializers import UserSerializer,PakgSerializer,BookingSerializer
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework import viewsets 
# Create your views here.

#For User

class UserApi(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserCreated(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

#For Complaints
class PakgApi(viewsets.ModelViewSet):
    queryset=Pakg.objects.all()
    serializer_class=PakgSerializer

class BookingApi(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer