from django.shortcuts import render
from .models import User,Dest
from .serializers import UserSerializer,DestSerializer
from rest_framework.generics import CreateAPIView,ListAPIView

from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
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


class DestView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        Dests = Dest.objects.all()
        serializer = DestSerializer(Dests, many=True)
        return Response(serializer.data)

    def Dest(self, request, *args, **kwargs):
        Dests_serializer = DestSerializer(data=request.data)
        if Dests_serializer.is_valid():
            Dests_serializer.save()
            return Response(Dests_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', Dests_serializer.errors)
            return Response(Dests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)