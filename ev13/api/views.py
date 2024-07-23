from .models import Student
from .serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet

class StudentModelViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentReadonly(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer