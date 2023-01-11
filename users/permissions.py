from rest_framework import permissions
from .models import User
from rest_framework.views import View, Request


class IsAccountOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        account_owner = request.user.is_authenticated and obj == request.user
        superuser = request.user.is_superuser
        return account_owner or superuser


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        account_owner = request.user.is_authenticated and obj.user == request.user

        return account_owner


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method == "POST"
            or request.user.is_authenticated
            and request.user.is_superuser
        )
