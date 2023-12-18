from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import Studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body            #used to catch data
        stream = io.BytesIO(json_data)          # Create a BytesIO stream from the JSON data.
        python_data = JSONParser().parse(stream)        # Use the JSONParser to parse the JSON data into Python data.
        serializer = Studentserializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type = 'application/json')
            return JsonResponse(serializer.data)
        json_data = JSONRenderer().render(serializer.errors)        #Render JSON-formatted validation errors.
        return HttpResponse(json_data,content_type = 'application/json')

