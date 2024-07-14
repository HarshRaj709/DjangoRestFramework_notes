from django.shortcuts import render,HttpResponse
from .models import Student
from .seriealizers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse

# Create your views here.
def home(request):
    students = Student.objects.all()
    serializers = StudentSerializer(students,many = True)
    print(serializers)
    return JsonResponse(serializers.data,safe = False)      # safe = False it is necessary when we are passing multiple data
    # jsondata = JSONRenderer().render(serializers.data)
    # print(jsondata)
    # return HttpResponse(jsondata,content_type = 'application/json')
