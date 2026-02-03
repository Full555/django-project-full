from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from core.models import Booking, ServiceType, Master, Services
#
#
# class BookingFilter(FilterSet):
#     name = CharFilter(field_name='name', lookup_expr='icontains')
#
#     service = ModelChoiceFilter(queryset=ServiceType.objects.all(), field_name='service')
#
#     master = ModelChoiceFilter(queryset=Master.objects.all(), field_name='master')
#
#     date = DateFilter(field_name='date', lookup_expr='exact')
#     date__gte = DateFilter(field_name='date', lookup_expr='gte')
#     date__lte = DateFilter(field_name='date', lookup_expr='lte')
#
#     created_at__gte = DateFilter(field_name='created_at', lookup_expr='gte')
#     created_at__lte = DateFilter(field_name='created_at', lookup_expr='lte')
#
#     class Meta:
#         model = Booking
#         fields = [
#             'name',
#             'service',
#             'master',
#             'date',
#             'date__gte',
#             'date__lte',
#             'created_at__gte',
#             'created_at__lte',
#         ]


class MasterFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    typename = ModelChoiceFilter(queryset=ServiceType.objects.all(), field_name='typename')
    experience = CharFilter(field_name='experience', lookup_expr='icontains')

    class Meta:
        model = Master
        fields = [
            'name',
            'typename',
            'experience',
        ]


class ServicesFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    typename = ModelChoiceFilter(queryset=ServiceType.objects.all(), field_name='typename')
    money__gte = CharFilter(field_name='money', lookup_expr='gte')
    money__lte = CharFilter(field_name='money', lookup_expr='lte')

    class Meta:
        model = Services
        fields = [
            'name',
            'typename',
            'money__gte',
            'money__lte',
        ]
