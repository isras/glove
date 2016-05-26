from django.contrib import admin
from .models import Enterprise, Driver, Customer, TypeService, Coupon, History, Order

# Register your models here.
admin.site.register(Enterprise)
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(TypeService)
admin.site.register(Coupon)
admin.site.register(History)
admin.site.register(Order)
