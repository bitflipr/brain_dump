from django.conf.urls import patterns, include, url

urlpatterns = patterns('brain_dump.views',
    url(r'^$', 'index'),
    url(r'^(?P<dump_id>\d+)/$', 'detail'),
)
