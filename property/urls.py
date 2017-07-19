from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.property_list, name='property_list'),
]
