from rest_framework import serializers
from .models import User,Dest



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','fname','lname','uemail','upassword','urpassword']


class DestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dest
        fields='__all__'
        

        
