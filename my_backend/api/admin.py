from django.contrib import admin
from .models import Booking, Pakg, User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id',"fname","lname","uemail","upassword","urpassword"]

@admin.register(Pakg)
class PakgAdmin(admin.ModelAdmin):
    list_display=["id","pImg","price","pdurat","ptitle","prating"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=["id","uname","bemail","bphone","btickettype","badult","bchild","bmessage"]