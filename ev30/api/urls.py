from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

routers = DefaultRouter()
routers.register('StudentApi',views.Studentlist,basename='Everything')
routers.register('StudentApi2',views.Userlogin,basename='login')

urlpatterns = [
    path('',include(routers.urls)),
    path('register/',views.StudentRegister.as_view(),name='register'),

]
