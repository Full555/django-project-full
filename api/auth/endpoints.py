from django.urls import path
from .generic_api import RegisterAPIView, LoginAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]