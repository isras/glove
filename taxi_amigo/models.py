from decimal import Decimal

from django.db import models
from userprofiles.models import User


class ValueSettings(models.Model):
    COUPON_VALUE = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    COUPON_NEW_USER_VALUE = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)


class ServiceType(models.Model):
    service_name = models.CharField(max_length=200)
    type_image = models.ImageField(upload_to='service_type')
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name


class Driver(models.Model):
    latitude = models.CharField(default=0.0000000, max_length=200)
    longitude = models.CharField(default=0.0000000, max_length=200)
    notification_id = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    service_type = models.ForeignKey(ServiceType)
    app_user = models.ForeignKey(User)

    def __str__(self):
        return self.app_user.first_name + " " + self.app_user.last_name


class Customer(models.Model):
    born_date = models.DateField('fecha de nacimiento')
    phone = models.CharField(max_length=20, default='phone number')
    home_address = models.CharField(max_length=150)
    work_address = models.CharField(max_length=150)
    app_user = models.ForeignKey(User)

    def __str__(self):
        return self.app_user.first_name + " " + self.app_user.last_name


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(blank=True)
    description = models.TextField(max_length=250, blank=True)
    status = models.BooleanField(default=True)
    expires = models.DateTimeField(blank=True)
    coupon_value = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, blank=True)
    customer = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_customer', on_delete=models.CASCADE,
                                 blank=True)
    driver = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_driver', on_delete=models.CASCADE,
                               blank=True, null=True)

    def __str__(self):
        return self.description


class Delivery(models.Model):
    name = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250, blank=True)
    initial_address = models.CharField(max_length=250, blank=True)
    initial_latitude = models.CharField(default=0.0000000, max_length=200, blank=True)
    initial_longitude = models.CharField(default=0.000000, max_length=200, blank=True)
    destination_address = models.CharField(max_length=250, blank=True)
    destination_latitude = models.CharField(default=0.0000000, max_length=200, blank=True)
    destination_longitude = models.CharField(default=0.000000, max_length=200, blank=True)
    date = models.DateTimeField(blank=True)
    reference = models.CharField(max_length=250, blank=True)
    delivery_total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, blank=True)
    state = models.CharField(max_length=50, blank=True)
    customer = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_customer', on_delete=models.CASCADE,
                                 blank=True)
    driver = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_driver', on_delete=models.CASCADE,
                               blank=True, null=True)


class BookTaxi(models.Model):
    date = models.DateTimeField()
    hour = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=250, blank=True)
    latitude = models.CharField(default=0.000000, max_length=200, blank=True)
    longitude = models.CharField(default=0.00000, max_length=200, blank=True)
    reference = models.CharField(max_length=250, blank=True)
    destination_address = models.CharField(max_length=250, blank=True)
    destination_latitude = models.CharField(default=0.000000, max_length=200, blank=True)
    destination_longitude = models.CharField(default=0.00000, max_length=200, blank=True)
    state = models.CharField(max_length=50, blank=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True)
    customer = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_customer', on_delete=models.CASCADE,
                                 blank=True)
    driver = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_driver', on_delete=models.CASCADE,
                               blank=True, null=True)


class CabRide(models.Model):
    date = models.DateTimeField(blank=True)
    initial_address = models.CharField(max_length=250, default='initial_address')
    final_address = models.CharField(max_length=250, default='final_address')
    career_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.0'))
    state = models.CharField(max_length=100, blank=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True)
    customer = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_customer', on_delete=models.CASCADE,
                                 blank=True)
    driver = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_driver', on_delete=models.CASCADE,
                               default='1', blank=True, null=True)


class Taxi(models.Model):
    plaque = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    driver = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_driver', on_delete=models.CASCADE,
                               blank=True, null=True)
