from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import Studentserializers


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def home(request,pk=None):
    if request.method == 'GET':
        id = pk           #request.data.get('id')
        if id:
            stu = Student.objects.get(pk=id)
            serialize = Studentserializers(stu)
            return Response(serialize.data)
        else: 
            stu = Student.objects.all()
            serialize = Studentserializers(stu,many=True)
            return Response(serialize.data)
    
    if request.method == 'POST':
        serialize = Studentserializers(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg':'data created successfully','data':serialize.data})
        return Response(serialize.errors)
    
    if request.method == 'PUT':
        id =    pk
        stu = Student.objects.get(pk=id)
        serialize = Studentserializers(stu,data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
    

    if request.method == 'PATCH':
        id =pk
        stu = Student.objects.get(pk=id)
        serialize = Studentserializers(stu,data = request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg':'partial data updated'})
        return Response(serialize.errors)
        
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':f"id {id} is deleted "})
    