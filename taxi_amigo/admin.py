from django.contrib import admin
from userprofiles.models import User
from .models import Driver, Customer, ServiceType, Coupon, CabRide, BookTaxi, Delivery

# Register your models here.
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(ServiceType)
admin.site.register(User)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('customer', 'coupon_code', 'description', 'date', 'status', 'expires')


admin.site.register(Coupon, CouponAdmin)


class CabRideAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'service_type', 'initial_address', 'final_address', 'state', 'career_total')


admin.site.register(CabRide, CabRideAdmin)


class BookTaxiAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service_type', 'date', 'hour', 'address', 'reference')


admin.site.register(BookTaxi, BookTaxiAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'name', 'description', 'initial_address', 'destination_address', 'date', 'reference', 'driver')


admin.site.register(Delivery, DeliveryAdmin)