# Rest framework
from rest_framework import generics, permissions, authentication, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

# Serializers
from .serializer import RoomSerializer

# Knox
from knox.models import AuthToken
from knox.auth import TokenAuthentication

# Models
from .models import Room

class GetRooms(generics.GenericAPIView):

  permission_classes = (IsAuthenticated,)

  def get(self, request):
    serializer = RoomSerializer(Room.objects.all(), many=True)
    return Response(serializer.data)