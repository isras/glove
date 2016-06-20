from taxi_amigo.models import Driver, ServiceType, Customer
from .serializers import DriverSerializer, ServiceTypeSerializer, CustomerSerializer

from rest_framework import viewsets


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class TypeServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()