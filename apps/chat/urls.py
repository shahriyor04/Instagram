
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ChatModelViewSet


router = DefaultRouter()
router.register('message', ChatModelViewSet, 'posts')
urlpatterns = [
    path('', include(router.urls))
]
