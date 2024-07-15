from django.shortcuts import render
from .models import Student
from .serializers import Studentserializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        body = request.body
        stream = io.BytesIO(body)
        python_data = JSONParser().parse(stream)
        serializer = Studentserializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data saved successfully'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serializer.errors,safe = False)