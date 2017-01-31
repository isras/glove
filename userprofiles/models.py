from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    service_type = models.IntegerField(default=1, blank=True, null=True)
    available = models.BooleanField(default=True, blank=True)
    latitude = models.DecimalField(default=0.0000000, max_digits=10, decimal_places=10, blank=True)
    longitude = models.DecimalField(default=0.0000000, max_digits=10, decimal_places=10, blank=True)
    player_id = models.CharField(default="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", max_length=200, blank=True)
    phone = models.CharField(default="xxx-xxxxxxx", max_length=50, blank=True)
    address = models.CharField(default="", max_length=200, blank=True)
    mobile_phone = models.CharField(default="xxx-xxxxxxx", max_length=50, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'auth_user'
