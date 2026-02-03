# from rest_framework.permissions import BasePermission, SAFE_METHODS
#
# class BookingPermission(BasePermission):
#
#     def has_permission(self, request, view):
#
#         if request.method in SAFE_METHODS:
#             return True
#
#
#         return False

from rest_framework.permissions import BasePermission, SAFE_METHODS

class BookingPermission(BasePermission):

    def has_permission(self, request, view):


        if request.method in SAFE_METHODS:
            return True


        if request.method == 'POST' and request.user.is_authenticated:
            return True

        return False
