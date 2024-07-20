from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',views.Studentget.as_view(),name='home'),
    path('api/<int:pk>/',views.StudentRetrieve.as_view(),name='retrieve'),
    path('api/update/<int:pk>/',views.StudentUpdate.as_view(),name='update'),
    path('api/delete/<int:pk>/',views.Studentdelete.as_view(),name='delete'),
]
