from django.db import models
from django.contrib.auth.models import User


class ServiceType(models.Model):
    service_name = models.CharField(max_length=200)
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
    phone = models.CharField(max_length=20)
    app_user = models.ForeignKey(User)

    def __str__(self):
        return self.app_user.first_name + " " + self.app_user.last_name


class Coupon(models.Model):
    description = models.TextField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class History(models.Model):
    description = models.CharField(max_length=250)
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Order(models.Model):
    description = models.CharField(max_length=250)
    date = models.DateTimeField()
    state = models.CharField(max_length=100)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    customer = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
