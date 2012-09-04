# Create your views here.
from brain_dump.models import Dump
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
  dump_list = Dump.objects.all().order_by('date')
  return render_to_response('dumps/index.html', {'dump_list': dump_list})

def detail(request, dump_id):
  dump = get_object_or_404(Dump, pk=dump_id)
  return render_to_response('dumps/detail.html', {'dump': dump})
