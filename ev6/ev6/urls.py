from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('views/',views.home,name='home'),
    path('student_create/',views.student_create,name='create'),
]
