from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
# Create your views here.

class StudentApi(ModelViewSet):
    queryset = Student.objects.all()            #filter(passby = 'jaiveer')
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    filterset_fields = ['city','name']

class StudentList(ListAPIView):         #non default filters
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city','name']

