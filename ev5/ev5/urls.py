from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name = 'home'),
    path('data/',views.data,name='data')
]
