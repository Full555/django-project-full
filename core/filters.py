import django_filters
from .models import Master, Photo, Feedback

class MasterFilter(django_filters.FilterSet):
    typename = django_filters.NumberFilter(field_name='typename_id')

    class Meta:
        model = Master
        fields = ['typename']

class PhotoFilter(django_filters.FilterSet):
    typename = django_filters.NumberFilter(field_name='typename_id')

    class Meta:
        model = Photo
        fields = ['typename']

class FeedbackFilter(django_filters.FilterSet):
    typename = django_filters.NumberFilter(field_name='typename_id')

    class Meta:
        model = Feedback
        fields = ['typename']



