from rest_framework import serializers
from .models import Singer,Songs


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = "__all__"


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True)
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)     #not happend anything
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Songs-detail')
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='Musician')
    song = serializers.HyperlinkedIdentityField(view_name='Songs-detail')
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']      #song is working because we used that name as related name.

