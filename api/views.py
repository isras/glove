from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from taxi_amigo.models import Driver, Order
from api.serializers import DriverSerializer, UserSerializer, OrderSerializer


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
