from django.urls import path
from .views import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('users/', User.as_view()),
    path('users/login/', TokenObtainPairView.as_view()),
    path('users/login/refresh/', TokenRefreshView.as_view()),
]