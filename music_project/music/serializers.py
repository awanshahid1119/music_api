

from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    user_profile = UserSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'user_profile']
