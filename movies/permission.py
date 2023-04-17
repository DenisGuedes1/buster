from rest_framework.permissions import BasePermission, IsAuthenticated
from users.models import User
#verifica se esta autenticado e se é um funcionario
class IsEmployee(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_employee
    
#verifica apenas se esta authenticado 
class AuthenticateUser(IsAuthenticated, BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

# class AuthUser(BasePermission):
#     def has_object_permission(self, request, view, obj: User):
         
#         return obj == request.user or request.user.is_employee

class AuthUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_employee:
            return True
        if obj == request.user:
            return True

        return False    