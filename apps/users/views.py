# # from django.http import JsonResponse
# # from rest_framework.authentication import TokenAuthentication
# # from rest_framework.parsers import MultiPartParser
# # from rest_framework.viewsets import ModelViewSet
# # from .serializers import RegisterSerializer, UserProfileSerializer
# # from .models import Registerlogin, UserProfile
# #
# # from rest_framework import viewsets
# #
# #
# # # from .models import krisi_user
# # from .permission import UserProfilePermissions
# # # from .serializers import krisi_user_serializers
# #
# #
# # class RegisterModelViewSet(ModelViewSet):
# #     serializer_class = RegisterSerializer
# #     queryset = Registerlogin.objects.all()
# #
# #
# # # class Krisi_user_view(viewsets.ModelViewSet):
# # #     queryset = krisi_user.objects.all()
# # #     serializer_class = krisi_user_serializers
# # #     parser_classes = MultiPartParser
# # #
# # #     def post(self, request, format=None):
# # #         serializer = krisi_user_serializers(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return JsonResponse(serializer.data)
# # #         return JsonResponse(serializer.errors, status=400)
# #
# #
# # class UserProfileViewSet(ModelViewSet):
# #     queryset = UserProfile.objects.all()
# #     serializer_class = UserProfileSerializer
# #     permission_classes = (UserProfilePermissions, )
# from django.contrib.auth.models import User
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.viewsets import ModelViewSet
#
# from users.models import UserProfile
# from users.serializers import UserProfileSerializer, UserSerializer
#
# from .permission import UserProfilePermissions, UpdateOwnUser
#
#
#
#
# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [UpdateOwnUser]
#     serializer_class = UserSerializer
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     filterset_fields = ["username"]
#     search_fields = ["username"]
#
#
# class UserProfileViewSet(ModelViewSet):
#     queryset = UserProfile.objects.all()
#     # authentication_classes = [TokenAuthentication]
#     serializer_class = UserProfileSerializer
#     permission_classes = [UserProfilePermissions]
