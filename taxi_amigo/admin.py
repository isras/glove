from django.contrib import admin
from .models import Driver, Customer, ServiceType, Coupon, CabRide, BookTaxi, Delivery

# Register your models here.
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(ServiceType)
admin.site.register(Coupon)


class CabRideAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'service_type', 'initial_address', 'final_address', 'state', 'career_total')
admin.site.register(CabRide, CabRideAdmin)


class BookTaxiAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service_type', 'date', 'hour', 'address', 'reference')
admin.site.register(BookTaxi, BookTaxiAdmin)
admin.site.register(Delivery)
