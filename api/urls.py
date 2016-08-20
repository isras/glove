from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'drivers/$', views.drivers_url),
    url(r'^drivers/(?P<pk>[0-9]+)/$', views.DriverDetail.as_view()),
    url(r'users/$', views.UserList.as_view()),
    url(r'cab_rides/$', views.CabRideList.as_view()),
    url(r'cab_rides/(?P<pk>[0-9]+)/$', views.CabRideDetail.as_view()),
    url(r'customers/$', views.CustomerList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url(r'^coupons/$', views.CouponList.as_view()),
]
