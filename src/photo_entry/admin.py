from django.contrib import admin
from zinnia.models import Entry
from zinnia.admin.entry import EntryAdmin
from django.utils.translation import ugettext_lazy as _

class PhotoEntryAdmin( EntryAdmin ):
	
	fieldsets = ((_('Content'), {'fields': (
		'title', 'content', 'image', 'status', 'photo', 'palette')})) + \
		EntryAdmin.fieldsets[1:]

admin.site.unregister(Entry)
admin.site.register(Entry, PhotoEntryAdmin)
