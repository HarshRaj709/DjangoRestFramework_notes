from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

#create Router Object
router = DefaultRouter()

#Register StudentViewSet with Router
# router.register('starting path',view's class,basename='Student')
router.register('Studentapi',views.StudentViewset,basename='Student')       #/<int:pk>/ this will handle by router


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls)),
]
