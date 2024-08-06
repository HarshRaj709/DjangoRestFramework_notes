from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()
router.register('StudentApi',views.StudentApi,basename='basic')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),        #http://127.0.0.1:8000/StudentApi/?username=rohan to acess
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),   #http POST http://127.0.0.1:8000/gettoken/ username='user1' password="geekyshows"
    path('token_refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verify_token/',TokenVerifyView.as_view(),name='verify_token'),
]
