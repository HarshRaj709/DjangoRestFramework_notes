from .models import Student
from .serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class StudentModelViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]                #wrote in setting.py file
    # permission_classes = [IsAdminUser]          #IsAuthenticated

class StudentReadonly(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer