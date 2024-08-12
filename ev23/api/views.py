from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

# Create your views here.

class StudentApi(ModelViewSet):
    queryset = Student.objects.all()            #filter(passby = 'jaiveer')
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    
    
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)

