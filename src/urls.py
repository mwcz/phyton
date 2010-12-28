from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # serve static media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/zip/workspace/clayto/branches/clayto_2/media', 'show_indexes': True}),

    (r'^photo/(?P<photo_slug>.*)$', 'photos.views.photo' ),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/photos/photo/$', 'clayto_2.photos.admin_views.change'),
    (r'^admin/', include(admin.site.urls)),
)
