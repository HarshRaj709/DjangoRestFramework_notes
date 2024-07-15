from rest_framework import serializers
from .models import Student

def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name should start with r')
    

class Studentserializers(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators = [start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self,validate_value):
        return Student.objects.create(**validate_value)

#field Level Validation
    def validate_name(self,value):
        if Student.objects.filter(name = value):
            raise serializers.ValidationError('name already used')
        return value


    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Greater than 200')
        return value

#Object Level Validation
    def validate(self,data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'rohan' and city.lower() != 'ranchi':
            raise serializers.ValidationError('city must be ranchi')
        return data