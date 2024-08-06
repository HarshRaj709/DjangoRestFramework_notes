from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('StudentApi',views.StudentApi,basename='basic')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))        #http://127.0.0.1:8000/StudentApi/?username=rohan to acess
]
