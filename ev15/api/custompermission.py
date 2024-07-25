from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':            #"detail": "You do not have permission to perform this action."
            return True     #means allow to access
        return False