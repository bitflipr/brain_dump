from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from brain_dump.models import Dump

urlpatterns = patterns('',
    url(r'^$', 'brain_dump.views.index'),
    url(r'^(?P<pk>\d+)/$',
      DetailView.as_view(
        model=Dump,
        template_name='dumps/detail.html'),
      name='dump_detail'),
    url(r'^(?P<dump_id>\d+)/edit/$', 'brain_dump.views.edit'),
    url(r'^(?P<dump_id>\d+)/follow_up/$', 'brain_dump.views.follow_up'),
    url(r'^new/$', 'brain_dump.views.new'),
    url(r'^add/$', 'brain_dump.views.add'),
    url(r'^signout/$', 'brain_dump.views.sign_out'),
)
