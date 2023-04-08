from django.urls import path, include
from rest_framework import routers
from .views import LinkMapViewSet, redirect

router = routers.DefaultRouter()
router.register('', LinkMapViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<str:url>', redirect, name='redirect')
]