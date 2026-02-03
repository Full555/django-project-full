from rest_framework import serializers
from core.models import Booking, Master, Services, Feedback


class BookingSerializer(serializers.ModelSerializer):


    class Meta:
        model = Booking
        fields = '__all__'

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MasterSerializer(serializers.ModelSerializer):

    typename = serializers.CharField(source='typename.name', read_only=True)

    class Meta:
        model = Master
        fields = ['id', 'image', 'name', 'experience', 'information', 'typename']



class ServiceSerializer(serializers.ModelSerializer):

    typename = serializers.CharField(source='typename.name', read_only=True)

    class Meta:
        model = Services
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    typename = serializers.CharField(source='typename.name', read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'