from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.booking_list, name='booking_list'),
    url(r'^(?P<pk>\d+)/$', views.booking_detail, name='booking_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.booking_edit, name='booking_edit'),
]
