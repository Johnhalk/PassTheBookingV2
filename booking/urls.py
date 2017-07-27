from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BookingList.as_view(), name='booking_list'),
    url(r'^(?P<pk>\d+)/$', views.BookingDetail.as_view(), name='booking_detail'),
    url(r'^new/$', views.CreateBooking.as_view(), name='booking_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.EditBooking.as_view(), name='booking_edit'),
]
