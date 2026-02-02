from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from .paginations import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Booking, Master, Services, Feedback
from .serializers import BookingSerializer, MasterSerializer, ServiceSerializer, FeedbackSerializer
from .filters import BookingFilter, MasterFilter, ServicesFilter


class BookingViewSet(ReadOnlyModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookingFilter


class MasterViewSet(ReadOnlyModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MasterFilter


class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ServicesFilter


class FeedbackViewSet(ReadOnlyModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = (DjangoFilterBackend,)
