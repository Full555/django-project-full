from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .paginations import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Booking, Master, Services, Feedback
from .serializers import BookingSerializer, MasterSerializer, ServiceSerializer, FeedbackSerializer, BookingCreateSerializer
from .filters import  MasterFilter, ServicesFilter
from .permissions import BookingPermission

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    pagination_class = StandardResultsSetPagination
    permission_classes = [BookingPermission]

    def get_serializer_class(self):
        if self.action == 'list':
          return BookingSerializer
        elif self.action == 'create':
            return BookingCreateSerializer
        return BookingSerializer


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
