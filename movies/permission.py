from rest_framework.permissions import IsAuthenticated, BasePermission


class IsEmployee(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_employee

class IsSuperUserOrRead(IsAuthenticated, BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated and request.user.is_superuser
        return request.user.is_authenticated