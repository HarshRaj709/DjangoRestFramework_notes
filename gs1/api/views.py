from django.shortcuts import render,HttpResponse
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse            #used to eliminate 2 lines


# Create your views here.
# def student_details(request):
#     stu = Student.objects.get(id=3)         #specifying which objects data we want?
#     serializer = StudentSerializers(stu)        #here we serialized our data----> complex data to python native datatype
#     print(serializer)
#     json_data = JSONRenderer().render(serializer.data)      #rendering our python native datatype to jsondata.
#     return HttpResponse(json_data,content_type = 'application/json')


#passing all data in single time

def student_details2(request,pk):
    stu = Student.objects.get(id=pk)         #specifying which objects data we want?
    serializer = StudentSerializers(stu)        #here we use all students data so we have to make many = True
    print(serializer)
    # json_data = JSONRenderer().render(serializer.data)      #rendering our python native datatype to jsondata.
    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data)    #ye chal rha h kyoki single item dictionary me h.


def student_details(request):
    stu = Student.objects.all()         #specifying which objects data we want?
    serializer = StudentSerializers(stu,many = True)        #here we use all students data so we have to make many = True
    print(serializer)
    # json_data = JSONRenderer().render(serializer.data)      #rendering our python native datatype to jsondata.
    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data,safe=False)            #In order to allow non-dict objects to be serialized set the safe parameter to False.
    