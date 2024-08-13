from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('StudentApi',views.StudentApi,basename='Everything')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('listview/',views.Acess.as_view(),name='list'),

]
