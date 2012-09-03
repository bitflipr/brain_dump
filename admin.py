from django.contrib import admin
from brain_dump.models import Dump, Link

class LinkInline(admin.TabularInline):
  model = Link
  extra = 0

class DumpAdmin(admin.ModelAdmin):
  inlines = [LinkInline]
  list_display = ('title', 'type', 'date', 'follow_up')
  list_filter = ['date']
  search_fields = ['title', 'description']

admin.site.register(Dump, DumpAdmin)
