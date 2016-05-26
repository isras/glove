from rest_framework import serializers
from taxi_amigo.models import Enterprise, Customer, Driver, TypeService, Coupon, History, Order


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('id', 'name', 'foundation_date', 'employee_number',)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'born_date', 'user', 'password',)


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'first_name', 'last_name', 'email', 'latitude', 'longitude', 'enterprise',)


class TypeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeService
        fields = ('id', 'service_name', 'rate', 'driver',)


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('id', 'description', 'customer',)


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'description', 'date', 'customer', 'driver',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'description', 'date', 'state', 'service_type', 'customer')
