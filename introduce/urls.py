"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views as intro_view

urlpatterns = [
    url(r'^$', intro_view.intro, name='intro'),
    url(r'^board/$', intro_view.board, name='board'),
    # url(r'^board_form/$', intro_view.board_form, name='board_form'),
    url(r'^detail/(?P<subject_id>[0-9]+)/$', intro_view.detail, name='detail'),
    url(r'^delete/(?P<subject_id>[0-9]+)/$', intro_view.delete, name='delete'),
    # url(r'^update/(?P<subject_id>[0-9]+)/$', intro_view.update, name='update'),

    url(r'^vote/(?P<subject_id>[0-9]+)/$', intro_view.vote, name='vote'),
    url(r'^result/(?P<subject_id>[0-9]+)/$', intro_view.result, name='result'),
]