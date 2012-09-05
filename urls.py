from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from brain_dump.models import Dump

class RequestListView(ListView):
  def get_context_data(self, **kwargs):
    #grab the context
    context = super(RequestListView, self).get_context_data(**kwargs)
    context.update({ 'request': self.request })
    return context

urlpatterns = patterns('',
    url(r'^$',
      RequestListView.as_view(
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
