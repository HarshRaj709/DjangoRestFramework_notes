from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self,data):
        name = data.get('name')
        roll = data.get('roll')

        if name.lower() == 'harsh' and roll == 101:
            raise serializers.ValidationError('developer name')
        return data