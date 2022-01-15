from rest_framework import permissions


class IsTeacher(permissions.BasePermission):
    """
    Global permission check for a user is teacher or not.
    """

    def has_permission(self, request, view):
        return hasattr(request.user, 'teacher')
