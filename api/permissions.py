from rest_framework import permissions


class IsAdminIsfahan(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser and request.user.is_superuser and request.user.phone.startswith('0913'):
            return True
        return False


class IsBuyer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.buyer == request.user
