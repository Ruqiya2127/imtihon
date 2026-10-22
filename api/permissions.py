from rest_framework.permissions import BasePermission, SAFE_METHODS

class AuthorBookPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if request.method == "POST":
            return request.user and request.user.is_authenticated

        if request.method in ['PUT', 'PACHT', 'DELETE']:
            return(request.user and request.user.is_authenticated and request.user.is_staff)
        return False