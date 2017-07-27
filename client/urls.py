from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.ClientList.as_view(), name='client_list'),
    url(r'^(?P<pk>\d+)/$', views.ClientDetail.as_view(), name='client_detail'),
    url(r'^new/$', views.CreateClient.as_view(), name='client_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.EditClient.as_view(), name='client_edit')
]
