from rest_framework import serializers
from taxi_amigo.models import Customer, Driver, ServiceType, Coupon, History, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class CustomerSerializer(serializers.ModelSerializer):
    app_user = UserSerializer

    class Meta:
        model = Customer
        fields = ('id', 'born_date', 'app_user')


class DriverSerializer(serializers.ModelSerializer):
    app_user = UserSerializer

    class Meta:
        model = Driver
        fields = ('id', 'latitude', 'longitude', 'avaliable', 'app_user', 'service_type')


class ServiceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceType
        fields = ('id', 'service_name', 'rate',)


class CouponSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Coupon
        fields = ('id', 'description', 'customer',)


class HistorySerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    driver = DriverSerializer()

    class Meta:
        model = History
        fields = ('id', 'description', 'date', 'customer', 'driver',)


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    service_type = ServiceTypeSerializer()

    class Meta:
        model = Order
        fields = ('id', 'description', 'date', 'state', 'service_type', 'customer')

