from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentInfo
from .serializers import StudentSerializers
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    students = StudentInfo.objects.all()
    serialized = StudentSerializers(students,many = True)
    return JsonResponse(serialized.data,safe=False)

@csrf_exempt
def send_data(request):
    if request.method == 'POST':
        json_data = request.body        #take its body      data b'{"name": "Harsh sahu", "roll": 101, "city": "hyderabad"}'
        stream = io.BytesIO(json_data)      #stream <_io.BytesIO object at 0x0000027A0F1ADF30>
        pythondata = JSONParser().parse(stream)     #pythondata {'name': 'Harsh sahu', 'roll': 101, 'city': 'hyderabad'}
        serializer = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data created'}
            return JsonResponse(res,safe = False)
        return JsonResponse(serializer.errors,safe=False)

