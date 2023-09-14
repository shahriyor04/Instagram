# from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import MessageSerializer
from .models import Message


class ChatModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post']
    # permission_classes = [IsAuthenticated]