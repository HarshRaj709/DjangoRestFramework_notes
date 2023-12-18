from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .models import Student
from .serializers import Studentserializer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)            #converted data to python data
        id = python_data.get('id',None)     # checking for id

        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = Studentserializer(stu)
            # return JsonResponse(serializer.data)
            json_data = JSONRenderer().render(serializer.data)          #converting back to json data.
            return HttpResponse(json_data,content_type='application/json')
        else:
            stu = Student.objects.all()
            serializer = Studentserializer(stu,many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)  
        python_data = JSONParser().parse(stream)        # converting json data to python data
        serializer = Studentserializer(data = python_data)      #conerting python data to complex data
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data saved successfully'}
            json_data = JSONRenderer().render(res)  #converting back python to json data type.
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)    #if serializer not get validate then pass errors.
        return HttpResponse(json_data,content_type='application/json')
    

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)  
        python_data = JSONParser().parse(stream)        # converting json data to python data
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = Studentserializer(stu,data = python_data,partial = True)       #as we are partially updating our data
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated successfully'}
            json_data = JSONRenderer().render(res)  #converting back python to json data type.
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)    #if serializer not get validate then pass errors.
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method =='DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted'}
        # json_data = JSONRenderer().render(res)  #converting back python to json data type.
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)
        