from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentApi',views.StudentModelViewset,basename='student-api')
router.register('Studentread',views.StudentReadonly,basename='student-read')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls))
]
