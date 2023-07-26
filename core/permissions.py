from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous:
            boolean = False
        elif user.role == 'cs':
            boolean = True
        else:
            boolean = False
        return boolean


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous:
            boolean = False
        elif user.role == 'sl':
            boolean = True
        else:
            boolean = False
        return boolean


class NotAllowed(BasePermission):
    def has_permission(self, request, view):
        return False


class Allowed(BasePermission):
    def has_permission(self, request, view):
        return True




