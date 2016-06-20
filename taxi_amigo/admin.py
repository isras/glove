from django.contrib import admin
from .models import Driver, Customer, ServiceType, Coupon, History, Order

# Register your models here.
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(ServiceType)
admin.site.register(Coupon)
admin.site.register(History)
admin.site.register(Order)
