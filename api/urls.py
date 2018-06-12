from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'coupons', views.CouponCodeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'drivers/$', views.UserDriverList.as_view()),
    url(r'^drivers/(?P<pk>[0-9]+)/$', views.DriverDetail.as_view()),
    url(r'^driver_cab_ride_history/(?P<username>.+)/$', views.DriverCabRideHistoryList.as_view()),
    url(r'^driver_delivery_history/(?P<username>.+)/$', views.DriverDeliveryHistoryList.as_view()),
    url(r'^driver_book_taxi_history/(?P<username>.+)/$', views.DriverBookTaxiHistoryList.as_view()),
    url(r'^driver_coupon_history/(?P<username>.+)/$', views.DriverCouponsHistoryList.as_view()),
    url(r'users/$', views.UserList.as_view()),
    url(r'cab_rides/$', views.CabRideList.as_view()),
    url(r'cab_rides/(?P<pk>[0-9]+)/$', views.CabRideDetail.as_view()),
    url(r'customers/$', views.UserCustomerList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url('^customer_cab_ride_history/(?P<username>.+)/$', views.CustomerCabRideHistoryList.as_view()),
    url('^customer_coupon_history/(?P<username>.+)/$', views.CustomerCouponsHistoryList.as_view()),
    url(r'^customer_delivery_history/(?P<username>.+)/$', views.CustomerDeliveryHistoryList.as_view()),
    url('^customer_book_taxi_history/(?P<username>.+)/$', views.CustomerBookTaxiHistoryList.as_view()),
    url(r'^coupons/$', views.CouponList.as_view()),
    url(r'^coupons/(?P<pk>[0-9]+)/$', views.CouponDetail.as_view()),
    url(r'^delivery/$', views.DeliveryList.as_view()),
    url(r'^delivery/(?P<pk>[0-9]+)/$', views.DeliveryDetail.as_view()),
    url(r'^book_taxi/$', views.BookTaxiList.as_view()),
    url(r'^book_taxi/(?P<pk>[0-9]+)/$', views.BookTaxiDetail.as_view()),
    url(r'^service_type/$', views.ServiceTypeList.as_view()),
    url(r'^value_settings/$', views.ValueSettingsList.as_view()),
    url(r'^taxi/$', views.TaxiList.as_view()),
    url(r'^taxi/(?P<pk>[0-9]+)/$', views.TaxiDetail.as_view()),
    url('^taxi_driver/(?P<id>.+)/$', views.TaxiOfDriver.as_view()),
    url('^taxi_user/(?P<id>.+)/$', views.DriverTaxi.as_view()),
    url(r'^cabride_costumer/(?P<id>.+)/$', views.LastCabRideByCostumerId.as_view()),
    url(r'^delivery_customer/(?P<id>.+)/$', views.LastDeliveryByCostumerId.as_view()),
    url(r'^cab_ride_count/(?P<pk>.+)/$', views.CabRideCountByUserView.as_view()),
    url(r'^book_taxi_count/(?P<pk>.+)/$', views.BookTaxiCountByUserView.as_view()),
    url(r'^delivery_count/(?P<pk>.+)/$', views.DeliveryCountByUserView.as_view()),
]
