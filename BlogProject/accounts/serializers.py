from rest_framework import serializers
from django.contrib.auth.models import User

class Registerserializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,required = True, error_messages = {'required':'Please provide password'})

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password']

    def validate(self,data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Username already used, try with other username')
        return data
    
    def create(self,validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'],
                                   email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data