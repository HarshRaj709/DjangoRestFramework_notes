from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('StudentApi',views.UserAuthentications,basename='Student-complete')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token),            #to obtain token from Api End points
]
