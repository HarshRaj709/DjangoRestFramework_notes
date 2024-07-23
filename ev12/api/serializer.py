from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        def validate_name(self,value):
            stu = Student.objects.filter(name=value)
            if stu:
                raise serializers.ValidationError('name already registered try with different name')
            return value
        
        def validate(self,data):
            roll = data.get('roll')
            city = data.get('city')
            if roll > 150 and city == 'lucknow':
                raise serializers.ValidationError('Please down your roll no. or change city name')
            return data
            
        