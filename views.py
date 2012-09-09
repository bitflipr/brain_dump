# Create your views here.
from brain_dump.models import Dump
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.template import RequestContext

def new(request):
  if request.user.has_perm('brain_dump.add_dump'):
    return render_to_response('dumps/new.html', context_instance=RequestContext(request))
  else:
    return HttpResponse('You do not have permission to add a Dump')

def add(request):
  if request.method == 'POST':
    title_added = request.POST['title']
    dump = Dump.objects.create(title=title_added)
    dump.save()  
    return HttpResponseRedirect(reverse('dump_index'))
  else:
    return HttpResponse('You cannot add a Dump using GET')

def sign_out(request):
  logout(request)
  return HttpResponseRedirect(reverse('dump_index'))
