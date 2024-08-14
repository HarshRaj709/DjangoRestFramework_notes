from rest_framework.viewsets import ModelViewSet
from .models import Singer,Songs
from .serializer import SingerSerializer,SongSerializer

# Create your views here.

class SingerSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongSet(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
