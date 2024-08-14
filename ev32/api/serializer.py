from rest_framework import serializers
from .models import Singer,Songs


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id','title','singer','Musician']

class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True, read_only=True)        #must use related_name only
    class Meta:
        model = Singer
        fields = ['id','name','song','gender']

