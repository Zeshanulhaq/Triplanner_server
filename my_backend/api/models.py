from django.db import models
from django.db.models.fields import NullBooleanField



def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.title), filename])

# Create your models here.

class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
 
    uemail=models.CharField(max_length=100,unique=True)
    upassword=models.CharField(max_length=100)
    urpassword=models.CharField(max_length=100)





    