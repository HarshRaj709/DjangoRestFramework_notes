from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializer import StudentSerializer
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentApi(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter,SearchFilter]
    search_fields = ['^name','^city']
    ordering_fields = '__all__'         #['city']

class Acess(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    authentication_classes = [SessionAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['^name']

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(name=user)

