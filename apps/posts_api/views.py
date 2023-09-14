from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from posts_api.models import Post
from posts_api.serializers import AuthorSerializer, PostSerializer


# Create your views here.

class PostAPIModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser]

