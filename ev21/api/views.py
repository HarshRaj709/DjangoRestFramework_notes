from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer
from .models import Student
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import JackRateThrottle

# Create your views here.
class StudentApi(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,JackRateThrottle]      #UserRateThrottle
