from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.Studentlist.as_view(),name='list')
]
