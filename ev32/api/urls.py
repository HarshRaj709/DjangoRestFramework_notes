from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Singer',views.SingerSet,basename='Singer')
router.register('Songs',views.SongSet,basename='Songs')


urlpatterns = [
    path('',include(router.urls)),
]
