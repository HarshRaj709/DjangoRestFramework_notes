from django.shortcuts import render
from .models import Student
from .serializers import Studentserilizers
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'POST':
        body = request.body
        stream = io.BytesIO(body)
        pythonData = JSONParser().parse(stream)
        serialized = Studentserilizers(data = pythonData)
        if serialized.is_valid():
            serialized.save()
            res = {'msg':'Entry added successfully'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serialized.errors,safe=False)
    
    if request.method == "GET":
        body = request.body
        stream = io.BytesIO(body)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)       #get id

        if id is not None:
            stu = Student.objects.get(pk = id)
            serialized = Studentserilizers(stu)
            return JsonResponse(serialized.data,safe=False)
        else:
            stu = Student.objects.all()
            serialized = Studentserilizers(stu,many = True)
            return JsonResponse(serialized.data,safe=False)
        
    if request.method == 'PUT':
        body = request.body
        stream = io.BytesIO(body)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        id  = python_data.get('id')
        student = Student.objects.get(id=id)
        stu = Studentserilizers(student,data=python_data,partial = True)        #to save data in databse we have to convert it first
        if stu.is_valid():
            stu.save()
            res = {'msg':'Data updated successfully'}
            return JsonResponse(res,safe=False)
        return JsonResponse(stu.errors,safe=False)
    
    if request.method == 'DELETE':
        body = request.body
        stream = io.BytesIO(body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        res = {'msg':f'id deleted with pk {id}'}
        return JsonResponse(res,safe=False)
