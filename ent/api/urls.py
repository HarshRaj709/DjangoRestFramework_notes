from django.urls import path
from .views import home_api

urlpatterns = [
    path('home/',home_api,name='home'),
]
