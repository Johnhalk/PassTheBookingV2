from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PropertyList.as_view(), name='property_list'),
    url(r'^(?P<pk>\d+)/$', views.PropertyDetail.as_view(), name='property_detail'),
    url(r'^new/$', views.CreateProperty.as_view(), name='property_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.EditProperty.as_view(), name='property_edit')
]
