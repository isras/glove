from django.conf.urls import url
from api import views

urlpatterns = [
    #url(r'^drivers/$', views.driver_list),
    #url(r'orders/$', views.order_list),
    url(r'drivers/$', views.drivers_url),
    url(r'^drivers/(?P<pk>[0-9]+)/$', views.DriverDetail.as_view()),
    url(r'users/$', views.UserList.as_view()),
]
