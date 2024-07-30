from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('StudentApi',views.StudentModelViewset,basename='Student-api')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))     #this is used to provide authentication form
]
