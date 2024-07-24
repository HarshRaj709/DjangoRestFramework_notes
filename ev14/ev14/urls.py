from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('StudentApi',views.StudentModelViewset,basename='student')
router.register('StudentApiread',views.StudentReadonly,basename='student-read')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls))
]
