
from django.conf.urls import url, include
from django.contrib import admin

from . import views as lotto_view

urlpatterns = [
    url(r'^$', lotto_view.index, name='index'),
    url(r'^new/$', lotto_view.new , name='new'),
    url(r'^detail/(?P<pk>[0-9]+)/$', lotto_view.detail, name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', lotto_view.update, name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', lotto_view.delete, name='delete')
]