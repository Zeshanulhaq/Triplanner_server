
from django.contrib import admin
from django.urls import path
from api import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.UserCreated.as_view()),
    path('api1/',views.UserList.as_view()),
   
    
]
