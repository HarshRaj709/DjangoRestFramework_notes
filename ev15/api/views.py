from .models import Student
from .serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermission import MyPermission

class StudentModelViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]                #this will not ask for credentials we have to add 1 line in urls.py
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [MyPermission]

class StudentReadonly(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    