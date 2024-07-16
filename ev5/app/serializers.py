from .models import Student
from rest_framework import serializers

def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')
    
class StudentSerializers(serializers.ModelSerializer):
    name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['id','roll']        #'__all__' not working here
        # extra_kwargs = {'name':{'read_only':True}}

    #get all create, update methods in-built

    # def validate_name(self,value):
    #     stu = Student.objects.filter(name = value)
    #     if stu:
    #         raise serializers.ValidationError('name already exist')
    #     return value


    # def validate(self,data):    
    #     name = data.get('name')
    #     city = data.get('city')
    #     if name.lower() == 'harsh' and city.lower() == 'kolkate':
    #         raise serializers.ValidationError('roll no. must be 100')
    #     return data 