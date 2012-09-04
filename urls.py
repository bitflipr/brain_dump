from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from brain_dump.models import Dump

urlpatterns = patterns('',
    url(r'^$',
      ListView.as_view(
        queryset=Dump.objects.order_by('-date'),
        context_object_name='dump_list',
        template_name='dumps/index.html'),
      name='dump_index'), 
    url(r'^(?P<pk>\d+)/$',
      DetailView.as_view(
        model=Dump,
        template_name='dumps/detail.html'),
      name='dump_detail'),
)
