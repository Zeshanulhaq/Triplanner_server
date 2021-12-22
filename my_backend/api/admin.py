from django.contrib import admin
from .models import User,Dest
# Register your models here.

@admin.register(User)
@admin.register(Dest)
class UserAdmin(admin.ModelAdmin):
    List_display=['id','fname','lname','uemail','upassword','urpassword']



