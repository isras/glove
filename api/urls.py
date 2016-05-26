from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^drivers/$', views.driver_list),
    url(r'orders/$', views.order_list),
]
