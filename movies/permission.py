from rest_framework.permissions import BasePermission, IsAuthenticated
from users.models import User

class IsEmployee(IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        if request.user.is_employee:
            return True
        if obj == request.user:
            return True
        return False  
          


class AuthenticateUser(IsAuthenticated, BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class AuthUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_employee:
            return True
        if obj == request.user:
            return True

        return False    