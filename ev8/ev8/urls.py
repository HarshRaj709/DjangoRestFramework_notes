from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',views.Studentviews.as_view(),name='home'),
    path('api/<int:pk>/',views.Studentviews.as_view(),name='home'),
]
