from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .class_api import BookingViewSet, MasterViewSet, ServiceViewSet, FeedbackViewSet

router = DefaultRouter()
router.register('booking', BookingViewSet, basename='booking')
router.register('master', MasterViewSet, basename='master')
router.register('service', ServiceViewSet, basename='service')
router.register('feedback', FeedbackViewSet, basename='feedback')
urlpatterns = [
path('', include(router.urls)),
]