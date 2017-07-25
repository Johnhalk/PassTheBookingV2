from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.property_list, name='property_list'),
    url(r'^(?P<pk>\d+)/$', views.property_detail, name='property_detail'),
    url(r'^new/$', views.property_new, name='property_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.property_edit, name='property_edit'),
]
