from django.urls import path, include
from rest_framework import routers

from .views import PersonViewSet, CommandViewSet


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'command', CommandViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
