from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    url(r'^(?P<pk>\d+)/$', views.client_detail, name='client_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit')
]
