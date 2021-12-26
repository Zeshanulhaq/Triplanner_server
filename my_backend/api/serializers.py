from rest_framework import serializers
from .models import Booking, User,Pakg

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id',"fname","lname","uemail","upassword","urpassword"]
        # def validate(self,data):
        #     upass=data.get('upassword')
        #     urpass=data.get('urpassword')
        #     ucnc=data.get('ucnic')
        #     if upass!=urpass:
        #         raise serializers.ValidationError('Password Does not Match')
        #     if ucnc<13 and ucnc>13:
        #         raise serializers.ValidationError('Length must be 13')

class PakgSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pakg
        fields= '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields= '__all__'