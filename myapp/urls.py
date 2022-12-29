from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet


router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refereshtoken/',TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    #path('createuser', views.CreateUser.as_view()),
    path('', include(router.urls)),
]