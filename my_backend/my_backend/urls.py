from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('userapi', views.UserApi)
router.register('Pakgapi', views.PakgApi)
router.register('bookingapi', views.BookingApi)



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api2/',views.ComplaintCreated.as_view()),
    # path('api3/',views.ComplaintList.as_view()),
    # path('api4/',views.OfficerList.as_view()),
    path('',include(router.urls)),
    
]
