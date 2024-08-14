from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Singer',views.SingerView,basename='Singer')
router.register('Songs',views.SongsView,basename='Songs')


urlpatterns = [
    path('',include(router.urls)),
]
