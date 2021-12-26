from django.db import models
# Create your models here.

class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    uemail=models.CharField(max_length=100, unique=True)
    upassword=models.CharField(max_length=100)
    urpassword=models.CharField(max_length=100)

class Pakg(models.Model):
    id=models.IntegerField(primary_key=True, auto_created=False)
    pImg=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    pdurat=models.CharField(max_length=100)
    ptitle=models.CharField(max_length=100)
    prating=models.CharField(max_length=100)

class Booking(models.Model):
    uname=models.CharField(max_length=100)
    bemail=models.CharField(max_length=100, unique=True)
    bphone=models.CharField(max_length=100)
    btickettype=models.CharField(max_length=100)
    badult=models.CharField(max_length=100)
    bchild=models.CharField(max_length=100)
    bmessage=models.CharField(max_length=5000)
