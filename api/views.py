from django.db.models import Count

from userprofiles.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from django_filters import rest_framework as filters
from rest_framework.renderers import JSONRenderer

from api.serializers import DriverSerializer, UserSerializer, CabRideSerializer, CustomerSerializer, CouponSerializer, \
    DeliverySerializer, BookTaxiSerializer, ServiceTypeSerializer, ValueSettingsSerializer, TaxiSerializer
from taxi_amigo.models import Driver, CabRide, Customer, Coupon, Delivery, BookTaxi, ServiceType, ValueSettings, Taxi


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


class TaxiList(APIView):
    serializer_class = TaxiSerializer

    def get(self, request, format=None):
        taxis = Taxi.objects.all()
        response = self.serializer_class(taxis, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        response = self.serializer_class(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxiDetail(APIView):
    """
    Obtener, actualizar o eliminar una solicitud de carrera
    """

    def get_object(self, pk):
        try:
            return Taxi.objects.get(pk=pk)
        except CabRide.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        taxi = self.get_object(pk)
        serializer = TaxiSerializer(taxi)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        taxi = self.get_object(pk)
        serializer = TaxiSerializer(taxi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        taxi = self.get_object(pk)
        taxi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDriverList(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        users = User.objects.filter(is_driver=1)
        response = self.serializer_class(users, many=True)
        return Response(response.data)


class UserCustomerList(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        users = User.objects.filter(is_customer=1)
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


class CouponDetail(APIView):
    """
    Obtener, actualizar o eliminar un conductor
    """

    def get_object(self, pk):
        try:
            return Coupon.objects.get(pk=pk)
        except Coupon.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        coupon = self.get_object(pk)
        serializer = CouponSerializer(coupon)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        coupon = self.get_object(pk)
        serializer = CouponSerializer(coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        coupon = self.get_object(pk)
        coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeliveryList(APIView):
    serializer_class = DeliverySerializer

    def get(self, request, format=None):
        deliveries = Delivery.objects.all()
        response = self.serializer_class(deliveries, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        response = self.serializer_class(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class DeliveryDetail(APIView):
    """
    Obtener, actualizar o eliminar un conductor
    """

    def get_object(self, pk):
        try:
            return Delivery.objects.get(pk=pk)
        except Delivery.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        delivery = self.get_object(pk)
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        delivery = self.get_object(pk)
        serializer = DeliverySerializer(delivery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        delivery = self.get_object(pk)
        delivery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookTaxiList(APIView):
    serializer_class = BookTaxiSerializer

    def get(self, request, format=None):
        book_taxies = BookTaxi.objects.all()
        response = self.serializer_class(book_taxies, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        response = self.serializer_class(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class BookTaxiDetail(APIView):
    """
    Obtener, actualizar o eliminar un conductor
    """

    def get_object(self, pk):
        try:
            return BookTaxi.objects.get(pk=pk)
        except BookTaxi.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book_taxi = self.get_object(pk)
        serializer = BookTaxiSerializer(book_taxi)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book_taxi = self.get_object(pk)
        serializer = BookTaxiSerializer(book_taxi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book_taxi = self.get_object(pk)
        book_taxi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceTypeList(APIView):
    serializer_class = ServiceTypeSerializer

    def get(self, request, format=None):
        service_types = ServiceType.objects.all()
        response = self.serializer_class(service_types, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        response = self.serializer_class(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class ValueSettingsList(APIView):
    serializer_class = ValueSettingsSerializer

    def get(self, request, format=None):
        value_settings = ValueSettings.objects.all()
        response = self.serializer_class(value_settings, many=True)
        return Response(response.data)


class CustomerCabRideHistoryList(generics.ListAPIView):
    serializer_class = CabRideSerializer

    def get_queryset(self):
        """
        Esta vista te devuelve la lista de todas las carreras solicitadas por el cliente
        determinadas por el username del cliente

        """
        username = self.kwargs['username']
        return CabRide.objects.filter(customer__username=username).order_by('-date')


class CustomerBookTaxiHistoryList(generics.ListAPIView):
    serializer_class = BookTaxiSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return BookTaxi.objects.filter(customer__username=username).order_by('-date')


class CustomerDeliveryHistoryList(generics.ListAPIView):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return Delivery.objects.filter(customer__username=username).order_by('-date')


class CustomerCouponsHistoryList(generics.ListAPIView):
    serializer_class = CouponSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return Coupon.objects.filter(customer__username=username).order_by('-date')


class CouponCodeViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all().order_by('-date')
    serializer_class = CouponSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('coupon_code',)


class DriverDeliveryHistoryList(generics.ListAPIView):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return Delivery.objects.filter(driver__username=username)


class DriverBookTaxiHistoryList(generics.ListAPIView):
    serializer_class = BookTaxiSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return BookTaxi.objects.filter(driver__username=username).order_by('-date')


class DriverCabRideHistoryList(generics.ListAPIView):
    serializer_class = CabRideSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return CabRide.objects.filter(driver__username=username).order_by('-date')


class DriverCouponsHistoryList(generics.ListAPIView):
    serializer_class = CouponSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return Coupon.objects.filter(driver__username=username).order_by('-date')


class TaxiOfDriver(generics.ListAPIView):
    serializer_class = TaxiSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        driver_id = self.kwargs['id']
        return Taxi.objects.filter(driver__id=driver_id)


class DriverTaxi(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user_id = self.kwargs['id']
        return User.objects.filter(id=user_id)


class LastCabRideByCostumerId(generics.ListAPIView):
    serializer_class = CabRideSerializer

    def get_queryset(self):
        """
        Esta vista va a retornar la ultima carrera de taxi solicitada por
        un usuario determinado por el id como parte de la URL.
        """
        customer_id = self.kwargs['id']
        return CabRide.objects.filter(customer__id=customer_id).order_by('-date')[:1]


class LastDeliveryByCostumerId(generics.ListAPIView):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        """
        Esta vista va a retornar la ultima carrera de taxi pidiendo una encomienda
        por un usuario determinado por el id como parte de la URL.
        """
        customer_id = self.kwargs['id']
        return Delivery.objects.filter(customer__id=customer_id).order_by('-date')[:1]


class CabRideCountByUserView(APIView):
    """
    Vista que devuelve el total de carreras solicitadas por cliente en JSON
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk, format=None):
        cab_ride_count = CabRide.objects.filter(customer=pk, state='finished').count()
        content = {'cab_ride_customer_count': cab_ride_count}
        return Response(content)


class BookTaxiCountByUserView(APIView):
    """
    Vista que devuelve el total de reservas solicitadas por cliente en JSON
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk, format=None):
        book_taxi_count = BookTaxi.objects.filter(customer=pk, state='finished').count()
        content = {'book_taxi_customer_count': book_taxi_count}
        return Response(content)


class DeliveryCountByUserView(APIView):
    """
    Vista que devuelve el total de reservas solicitadas por cliente en JSON
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk, format=None):
        delivery_count = Delivery.objects.filter(customer=pk, state='finished').count()
        content = {'delivery_customer_count': delivery_count}
        return Response(content)
