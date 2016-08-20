from rest_framework import serializers
from taxi_amigo.models import Customer, Driver, ServiceType, Coupon, CabRide
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'born_date', 'phone', 'app_user')


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ('id', 'latitude', 'longitude', 'available', 'app_user', 'service_type')


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id', 'service_name', 'rate',)


class CouponSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Coupon
        fields = ('id', 'coupon_code', 'date', 'description', 'status', 'expires', 'customer',)


class CabRideSerializer(serializers.ModelSerializer):

    class Meta:
        model = CabRide
        fields = (
            'id', 'date', 'initial_address', 'final_address', 'career_total', 'state', 'service_type',
            'customer', 'driver')
