from django.contrib import admin
from .models import Driver, Customer, ServiceType, Coupon, History, Order, BookCareer, Delivery

# Register your models here.
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(ServiceType)
admin.site.register(Coupon)
admin.site.register(History)


class CabCareerAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'service_type', 'initial_address', 'final_address', 'state', 'career_total')
admin.site.register(Order, CabCareerAdmin)


class BookCareerAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service_type', 'date', 'hour', 'address', 'reference')
admin.site.register(BookCareer, BookCareerAdmin)
admin.site.register(Delivery)
