from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',views.StudentList.as_view(),name='home'),
    path('api/<int:pk>/',views.StudentRetrieve.as_view(),name='retrieve'),
]
