from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.StudentRegister.as_view(),name='register')
]
