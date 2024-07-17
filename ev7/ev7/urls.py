from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',views.home,name='home'),
    path('api/<int:pk>',views.home,name='home'),
]
