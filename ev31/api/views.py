from rest_framework.viewsets import ModelViewSet
from .serializer import SingerSerializer,SongsSerializer
from .models import Songs,Singer

# Create your views here.
class SingerView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongsView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer