from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('send/',views.send_data,name='send'),
]
