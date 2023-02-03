from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet

router = routers.DefaultRouter()
router.register('persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]