from rest_framework import serializers
from .models import StudentInfo

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=150)

    def create(self,validate_data):
        return StudentInfo.objects.create(**validate_data)          #to store data
    