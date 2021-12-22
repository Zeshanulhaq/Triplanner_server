from django.shortcuts import render
from .models import User,Dest
from .serializers import UserSerializer,DestSerializer
from rest_framework.generics import CreateAPIView,ListAPIView

from rest_framework import viewsets
from django.http import HttpResponse
# from .serializers import DestSerializer
# from .models import Dest
# Create your views here.

#For User
class UserCreated(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class DestViewSet(viewsets.ModelViewSet):
    # queryset = Dest.objects.all()
    # serializer_class = DestSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Dest.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'Dest created'}, status=200)