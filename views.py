# Create your views here.
from brain_dump.models import Dump
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.template import RequestContext

import StringIO
import csv

def index(request):
  if request.user.is_authenticated():
    dump_list = Dump.objects.all()
  else:
    dump_list = Dump.objects.filter(private=False)

  dump_list = dump_list.order_by('date').reverse()

  return render_to_response(
    'dumps/index.html', 
    {'dump_list': dump_list}, 
    context_instance=RequestContext(request))

def new(request):
  if request.user.has_perm('brain_dump.add_dump'):
    return render_to_response('dumps/new.html', context_instance=RequestContext(request))
  else:
    return HttpResponse('You do not have permission to add a Dump')

def add(request):
  if request.method == 'POST':
    dump = Dump.objects.create(
      type=request.POST['type'],
      title=request.POST['title'],
      description=request.POST['description'])
    if 'follow_up' in request.POST and request.POST['follow_up'] == 'yes':
      dump.follow_up = True
    if 'private' in request.POST and request.POST['private'] == 'yes':
      dump.private = True
    if 'link' in request.POST and len(request.POST['link'])>0:
      link = dump.link_set.create(url=request.POST['link'])
    if 'tags' in request.POST and len(request.POST['tags'])>0:
      reader = csv.reader(StringIO.StringIO(request.POST['tags']), delimiter=',')
      for row in reader:
        for tag in row:
          dump.tags.add(tag)
    dump.save()  
    return HttpResponseRedirect(reverse('brain_dump.views.index'))
  else:
    return HttpResponse('You cannot add a Dump using GET')

def sign_out(request):
  logout(request)
  return HttpResponseRedirect(reverse('brain_dump.views.index'))
