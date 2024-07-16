from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializers = StudentSerializers(data = python_data)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'data created successfully'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serializers.errors,safe=False)
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(pk=id)
        serializers = StudentSerializers(stu,data = python_data,partial = True)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'data updated successfully'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serializers.errors,safe=False)
    
def data(request):
    stu = Student.objects.all()
    serializers = StudentSerializers(stu,many=True)
    return JsonResponse(serializers.data,safe=False)