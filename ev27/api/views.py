from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializer import StudentSerializer
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .pagination import CustomPage

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
    authentication_classes = [SessionAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['^name']
    pagination_class = CustomPage
