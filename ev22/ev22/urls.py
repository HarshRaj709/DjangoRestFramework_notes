from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('list/',views.StudentList.as_view(),name='create'),
    path('retrieve/',views.StudentRetrieve.as_view(),name='retrieve'),
]
