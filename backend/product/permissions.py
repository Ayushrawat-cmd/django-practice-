from rest_framework import permissions, request
from django.http.request import HttpRequest
class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request:HttpRequest, view):
        user = request.user
        print(user.get_all_permissions())    
        # if request.user.username == "cfe":
        #     return False
        if request.user.is_staff:
            return True
        return False
    
