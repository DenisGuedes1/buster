from django.urls import path
from .views import User
from rest_framework_simplejwt import views



urlpatterns = [
    path('users/', User.as_view()),
    path('users/login/', views.TokenObtainPairView.as_view()),
    path('users/login/refresh/', views.TokenRefreshView.as_view()),
]