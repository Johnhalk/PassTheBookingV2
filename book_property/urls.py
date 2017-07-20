from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_property_list, name='bookproperty_list'),
    url(r'^(?P<pk>\d+)/$', views.book_property_detail, name='bookproperty_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.book_property_edit, name='bookproperty_edit'),
]
