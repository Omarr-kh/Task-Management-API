from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.user_type == 'admin'


class IsClientUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.user_type == 'client'


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.profile == obj.user or request.user.profile.user_type == 'admin'
