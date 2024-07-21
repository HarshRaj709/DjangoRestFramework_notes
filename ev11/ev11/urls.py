from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',views.StudentListCreate.as_view(),name='home'),
    path('api/<int:pk>/',views.StudentRetrieveupdate.as_view(),name='home'),
]
