from django.db import models


# Create your models here.

class Enterprise(models.Model):
    name = models.CharField(max_length=200)
    foundation_date = models.DateField('fecha de fundacion')
    employee_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Driver(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    latitude = models.CharField(default=0.0000000, max_length=200)
    longitude = models.CharField(default=0.0000000, max_length=200)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name


class TypeService(models.Model):
    service_name = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    born_date = models.DateField('fecha de nacimiento')

    def __str__(self):
        return self.first_name + self.last_name


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
    service_type = models.ForeignKey(TypeService, on_delete=models.CASCADE)
    customer = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
