from django.urls import path
from . import views

urlpatterns = [
    path('stuinfo/',views.student_details,name='info'),
    path('stuinfo1/<int:pk>',views.student_details2,name='info2')
]
