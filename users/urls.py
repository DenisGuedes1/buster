from django.urls import path
from .views import UserView
from users.views import UserId
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/login/', TokenObtainPairView.as_view()),
    path('users/login/refresh/', TokenRefreshView.as_view()),
    path('users/<int:user_id>/', UserId.as_view()),
]