from django.contrib import admin
from django.urls import path,include
from api import views
import rest_framework


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',views.home,name='home'),
    path('api/<int:pk>',views.home,name='home'),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
