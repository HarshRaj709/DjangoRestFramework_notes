from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializer import StudentSerializer
from api.customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class StudentApi(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    #http http://127.0.0.1:8000/StudentApi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyOTMwNDIyLCJpYXQiOjE3MjI5MzAxMjIsImp0aSI6ImMzMjVhNzUyMTFkZTRhYzQ5YzUwNDVjNWQwZDJiZmEyIiwidXNlcl9pZCI6Mn0.gSlFeJ988T_8Ni09ILBo1N8sUMpeUCENPffjLw3mAxs'
    # to access databse.

    #http -f POST http://127.0.0.1:8000/StudentApi/ name=Raj roll=105 city=bokaro 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyOTMwOTAzLCJpYXQiOjE3MjI5MzA2MDMsImp0aSI6ImIxYWE3M2ExM2E3NjRkZDFhNTRlOTQ2Nzk0ZTQ0NTMyIiwidXNlcl9pZCI6Mn0.etdnU4MsF1gf-ZAFZg_WjrO6JPPJ5_t73G-yXl6PTwM'
    # to post data

    #http DELETE http://127.0.0.1:8000/StudentApi/3/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyOTMwOTAzLCJpYXQiOjE3MjI5MzA2MDMsImp0aSI6ImIxYWE3M2ExM2E3NjRkZDFhNTRlOTQ2Nzk0ZTQ0NTMyIiwidXNlcl9pZCI6Mn0.etdnU4MsF1gf-ZAFZg_WjrO6JPPJ5_t73G-yXl6PTwM'
    #to delete data


