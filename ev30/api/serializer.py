from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class Register(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required = True,error_messages={'required':'Password is neccessary'})
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def validate_username(self,value):
        if User.objects.filter(username = value).exists():
            raise serializers.ValidationError('Username already used')
        return value
    
    def create(self,validated_data):
        user = User.objects.create(username = validated_data['username'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],email=validated_data['email'])            #user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class Userlogin(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username','password']

