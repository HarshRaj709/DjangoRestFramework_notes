from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializer import StudentSerializer
from api.customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentApi(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]