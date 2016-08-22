from rest_framework import serializers
from taxi_amigo.models import Customer, Driver, ServiceType, Coupon, CabRide, Delivery, BookTaxi
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'born_date', 'phone', 'home_address', 'work_address', 'app_user')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'latitude', 'longitude', 'available', 'service_type', 'app_user',)


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


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('id', 'name', 'description', 'initial_address', 'destination_address', 'date', 'reference',
                  'customer', 'driver')


class BookTaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTaxi
        fields = ('id', 'date', 'hour', 'address', 'reference', 'service_type', 'customer', 'driver')
