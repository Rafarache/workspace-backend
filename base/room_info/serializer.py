from rest_framework import serializers
from room_info.models import Room

# User Serializer
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'address')