from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostAPIModelViewSet

router = DefaultRouter()
router.register('posts', PostAPIModelViewSet, basename='posts')


urlpatterns = [
    path('', include(router.urls)),
    # path('post1/', views.post, name="post1"),
]