from rest_framework import serializers
from enroll.models import User


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'