from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from .models import Message
from users.models import UserProfile


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'password']


class MessageSerializer(ModelSerializer):
    sender = SlugRelatedField(many=False, slug_field='fullname', queryset=UserProfile.objects.all())
    receiver = SlugRelatedField(many=False, slug_field='fullname', queryset=UserProfile.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
