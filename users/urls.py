from django.urls import path
from .views import User



urlpatterns = [
    path('users/', User.as_view())
]