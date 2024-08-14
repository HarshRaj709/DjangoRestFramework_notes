from .models import Student
from .serializer import StudentSerializer,Register,Userlogin
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token

# Create your views here.
class Studentlist(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentRegister(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = Register

#     def create(self,request,*args,**kwargs):            #it can work without args and kwargs
#         super().create(request)          
#         response_data = {'message': 'user registerd successfull'}
#         return Response(response_data,status=status.HTTP_201_CREATED)

class StudentRegister(CreateAPIView):       #for user registrations
    queryset = User.objects.all()
    serializer_class = Register


class Userlogin(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userlogin

    @action(detail=False,methods=['post'],url_path='login',url_name='login')
    def loginuser(self,request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username = username,password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


