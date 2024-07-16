from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])      #GET,POST,PUT,PATCH,DELETE  PUT-Update full data, PATCH- Update partial data
def home(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data entered'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)