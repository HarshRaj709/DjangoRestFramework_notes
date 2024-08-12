from rest_framework.generics import ListAPIView
from .serializer import Studentserializer
from .models import Student
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    filter_backends = [SearchFilter]
    # search_fields = ['=city']             # exact match
    search_fields = ['^city']           #starts with
    # search_fields = ['city']
