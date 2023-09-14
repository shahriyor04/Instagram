from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Post, Comment, Like
from users.models import UserProfile
from users.serializers import UserProfileSerializer


class AuthorSerializer(ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ["id", "fullname", "email", "profile"]
        depth = 1

        extra_kwargs = {"profile": {"read_only": True}}


class LikesSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Like
        fields = "__all__"

        extra_kwargs = {"author": {"read_only": True}}


class CommentSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

        extra_kwargs = {"author": {"read_only": True}}


class PostSerializer(ModelSerializer):
    likes = LikesSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_amount = serializers.SerializerMethodField("get_likes_amount")
    comments_amount = serializers.SerializerMethodField("get_comments_amount")
    author = AuthorSerializer(read_only=True)
    is_liked = serializers.SerializerMethodField("get_is_liked")

    class Meta:
        model = Post
        fields = [
            "id", "user", "description", "image", "is_liked", "likes", "likes_amount", "comments",
            "comments_amount", 'author',
        ]
        depth = 1

    @staticmethod
    def get_likes_amount(obj):
        return obj.likes.count()

    @staticmethod
    def get_comments_amount(obj):
        return obj.comments.count()

    def get_is_liked(self, obj):
        user = self.context["request"].user
        if user and not user.is_anonymous:
            return bool(obj.likes.filter(author=user))
        return None


class LikesDetailedSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = "__all__"

        extra_kwargs = {"author": {"read_only": True}}
