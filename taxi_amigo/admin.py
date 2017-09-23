from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi_amigo.forms import BookTaxiForm
from userprofiles.models import User
from .models import Driver, Customer, ServiceType, Coupon, CabRide, BookTaxi, Delivery, ValueSettings, Taxi

# Register your models here.
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(ServiceType)


class TaxiUserAdmin(UserAdmin):
    def get_fieldsets(self, request, obj=None):
        return super(TaxiUserAdmin, self).get_fieldsets(request, obj) + (
            ('Custom Fields', {'fields': ('is_driver', 'is_customer', 'service_type', 'available', 'latitude',
                                          'longitude', 'player_id', 'phone', 'address', 'mobile_phone')}),
        )


admin.site.register(User, TaxiUserAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('customer', 'coupon_code', 'description', 'date', 'status', 'expires')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "customer":
            kwargs["queryset"] = User.objects.filter(is_customer=1)

        return super(CouponAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Coupon, CouponAdmin)


class CabRideAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'date', 'service_type', 'initial_address', 'final_address', 'state', 'career_total', 'driver')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "driver":
            kwargs["queryset"] = User.objects.filter(is_driver=1)

        if db_field.name == "customer":
            kwargs["queryset"] = User.objects.filter(is_customer=1)

        return super(CabRideAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(CabRide, CabRideAdmin)


class BookTaxiAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service_type', 'date', 'hour', 'address', 'reference', 'driver')
    form = BookTaxiForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "driver":
            kwargs["queryset"] = User.objects.filter(is_driver=1)

        if db_field.name == "customer":
            kwargs["queryset"] = User.objects.filter(is_customer=1)

        return super(BookTaxiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(BookTaxi, BookTaxiAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'name', 'description', 'initial_address', 'destination_address', 'date', 'reference', 'driver')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "driver":
            kwargs["queryset"] = User.objects.filter(is_driver=1)

        if db_field.name == "customer":
            kwargs["queryset"] = User.objects.filter(is_customer=1)

        return super(DeliveryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(ValueSettings)


class TaxiAdmin(admin.ModelAdmin):
    list_display = (
        'driver', 'plaque', 'model', 'brand', 'color')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "driver":
            kwargs["queryset"] = User.objects.filter(is_driver=1)

        return super(TaxiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Taxi, TaxiAdmin)
