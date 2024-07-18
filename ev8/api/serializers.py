from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


    def validate_name(self,value):
        stu = Student.objects.filter(name=value)
        if stu:
            raise serializers.ValidationError('Name already present in databse')
        return value