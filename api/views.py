from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from taxi_amigo.models import Driver, CabRide, Customer, Coupon
from api.serializers import DriverSerializer, UserSerializer, CabRideSerializer, CustomerSerializer, CouponSerializer


# def index(request):
#   return HttpResponse("Estamos en el indice del api")

class DriverList(APIView):
    serializer_class = DriverSerializer

    def get(self, request, format=None):
        drivers = Driver.objects.all()
        response = self.serializer_class(drivers, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        response = self.serializer_class(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


drivers_url = DriverList.as_view()


class DriverDetail(APIView):
    """
    Obtener, actualizar o eliminar un conductor
    """

    def get_object(self, pk):
        try:
            return Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        driver = self.get_object(pk)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        driver = self.get_object(pk)
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        driver = self.get_object(pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        users = User.objects.all()
        response = self.serializer_class(users, many=True)
        return Response(response.data)


class CabRideList(APIView):
        serializer_class = CabRideSerializer

        def get(self, request, format=None):
            cab_rides = CabRide.objects.all()
            response = self.serializer_class(cab_rides, many=True)
            return Response(response.data)

        def post(self, request, format=None):
            response = self.serializer_class(data=request.data)
            if response.is_valid():
                response.save()
                return Response(response.data, status=status.HTTP_201_CREATED)
            return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class CabRideDetail(APIView):
    """
    Obtener, actualizar o eliminar una solicitud de carrera
    """

    def get_object(self, pk):
        try:
            return CabRide.objects.get(pk=pk)
        except CabRide.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cab_ride = self.get_object(pk)
        serializer = CabRideSerializer(cab_ride)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cab_ride = self.get_object(pk)
        serializer = CabRideSerializer(cab_ride, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cab_ride = self.get_object(pk)
        cab_ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerList(APIView):
    serializer_class = CustomerSerializer

    def get(self, request, format=None):
        customers = Customer.objects.all()
        response = self.serializer_class(customers, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        response = self.serializer_class(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """
    Obtener, actualizar o eliminar un conductor
    """

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CouponList(APIView):
    serializer_class = CouponSerializer

    def get(self, request, format=None):
        coupons = Coupon.objects.all()
        response = self.serializer_class(coupons, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        response = self.serializer_class(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)