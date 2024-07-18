from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status

# Create your views here.
class Studentviews(APIView):
    def get(self,request,format =None,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serialized = StudentSerializers(stu)
            return Response(serialized.data)
        stu = Student.objects.all()
        serialized = StudentSerializers(stu,many=True)
        return Response(serialized.data)
    
    def post(self,request,format=None):
        serialized = StudentSerializers(data=request.data)
        if serialized.is_valid():
            serialized.save()
            res = {'msg':'Data entered successfully'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serialized = StudentSerializers(stu,data = request.data)
        if serialized.is_valid():
            serialized.save()
            res={'msg':'data manipulated'}
            return Response(serialized.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serialized = StudentSerializers(stu,data=request.data,partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        res = {'msg':'Deleted'}
        return Response(res)
