from django.shortcuts import render
from .serializers import StudentSerializers
from django.http import JsonResponse
from .models import Students

# Create your views here.
def home(request):
    stu = Students.objects.all()
    serializer = StudentSerializers(stu,many=True)
    return JsonResponse(serializer.data,safe=False)

def stu(request):
    # student = Students.objects.get(pk=1)
    student = Students.objects.all()
    serial = StudentSerializers(student,many=True)
    context = {'student_data':serial.data}
    return render(request,'trial/student.html',context)