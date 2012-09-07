# Create your views here.
from brain_dump.models import Dump
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse

def sign_out(request):
  logout(request)
  return HttpResponseRedirect(reverse('dump_index'))
