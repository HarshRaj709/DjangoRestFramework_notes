from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_name(self,value):
        if Student.objects.filter(name=value).exists():
            raise serializers.ValidationError('Name already exists')
        return value