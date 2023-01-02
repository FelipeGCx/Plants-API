from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if "ADMIN_ROLE" in request.user.roles :
            return True
        return False