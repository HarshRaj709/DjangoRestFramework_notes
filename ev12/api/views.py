from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class StudentViewset(viewsets.ViewSet):
    def list(self,request):                     #it will automatically take Get,POST,PUT,PATCH,DELETE requests
        print('*******************LIST**********************')
        print("Basename:",self.basename)
        print("Action",self.action)
        print('Detail',self.detail)
        print('suffix',self.suffix)
        print('name',self.name)
        print('Description',self.description)
        
        stu = Student.objects.all()
        serialize = StudentSerializer(stu,many=True)
        return Response(serialize.data)
    
    def retrieve(self,request,pk=None):
        print('*******************RETRIEVE**********************')
        print("Basename:",self.basename)
        print("Action",self.action)
        print('Detail',self.detail)
        print('suffix',self.suffix)
        print('name',self.name)
        print('Description',self.description)
        id = pk
        if id:
            stu = Student.objects.get(pk=id)
            serialize = StudentSerializer(stu)
            return Response(serialize.data)
        
    def create(self,request):
        print('*******************CREATE**********************')
        print("Basename:",self.basename)
        print("Action",self.action)
        print('Detail',self.detail)
        print('suffix',self.suffix)
        print('name',self.name)
        print('Description',self.description)
        serialize = StudentSerializer(data=request.data)     #here data is dictionary
        if serialize.is_valid():
            serialize.save()
            return Response({'msg':'Data created successfully'})
        return Response(serialize.errors)
    
    def update(self,request,pk):
        print('*******************UPDATE**********************')
        print("Basename:",self.basename)
        print("Action",self.action)
        print('Detail',self.detail)
        print('suffix',self.suffix)
        print('name',self.name)
        print('Description',self.description)
        id=pk
        stu=Student.objects.get(pk=id)
        serialize = StudentSerializer(stu,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'data updated'})
        return Response(serialize.errors)

    def partial_update(self,request,pk):
        print('*******************PARTIAL UPDATE**********************')
        print("Basename:",self.basename)
        print("Action",self.action)
        print('Detail',self.detail)
        print('suffix',self.suffix)
        print('name',self.name)
        print('Description',self.description)
        id=pk
        stu = Student.objects.get(pk=id)
        serialize = StudentSerializer(stu,data=request.data,partial = True)
        if serialize.is_valid():
            serialize.save()
            return Response({'data updated'})
        return Response(serialize.errors)
    
    def destroy(self,request,pk):
        print('*******************DESTROY**********************')
        print("Basename:",self.basename)
        print("Action",self.action)
        print('Detail',self.detail)
        print('suffix',self.suffix)
        print('name',self.name)
        print('Description',self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg:data deleted successfully'})