from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == 'cs':
            boolean = True
        else:
            boolean = False
        return boolean


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == 'sl':
            boolean = True
        else:
            boolean = False
        return boolean





