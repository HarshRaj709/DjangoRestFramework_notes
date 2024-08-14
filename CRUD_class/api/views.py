from .serializers import ApiSerializer
from enroll.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class CRUDAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ApiSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]