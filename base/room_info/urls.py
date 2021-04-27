from .views import GetRooms
from django.urls import path

urlpatterns = [
    path('room/', GetRooms.as_view(), name='rooms'),
]