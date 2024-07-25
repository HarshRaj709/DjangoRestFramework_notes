from rest_framework import serializers
from .models import Student

class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = '__all__'