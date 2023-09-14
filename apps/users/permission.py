# from rest_framework.permissions import BasePermission, SAFE_METHODS
#
#
# class UserProfilePermissions(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user and SAFE_METHODS:
#             return True
#         return request.user.id == obj.id
#
#
# class UpdateOwnUser(BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#
#         if request.method in SAFE_METHODS:
#             return True
#
#         return request.user.id == obj.id
#
