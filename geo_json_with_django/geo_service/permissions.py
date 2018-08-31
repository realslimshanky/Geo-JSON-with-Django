from rest_framework import permissions


class IsProvider(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.provider.is_staff or request.method in permissions.SAFE_METHODS:
            return True
        return obj.provider == request.user
