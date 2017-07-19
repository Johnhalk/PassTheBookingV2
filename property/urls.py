from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.property_list, name='property_list'),
    url(r'^(?P<pk>\d+)/$', views.property_detail, name='property_detail'),
]
