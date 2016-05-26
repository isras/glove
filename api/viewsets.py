from taxi_amigo.models import Enterprise, Driver, TypeService, Customer
from .serializers import EnterpriseSerializer, DriverSerializer, TypeServiceSerializer, CustomerSerializer

from rest_framework import viewsets


class EnterpriseViewSet(viewsets.ModelViewSet):
    serializer_class = EnterpriseSerializer
    queryset = Enterprise.objects.all()


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class TypeServiceViewSet(viewsets.ModelViewSet):
    serializer_class = TypeServiceSerializer
    queryset = TypeService.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()