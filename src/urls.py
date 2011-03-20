from django.conf.urls.defaults import *
from django.contrib import admin
from settings import MEDIA_ROOT
from photos.feeds import RssPhotosFeed, AtomPhotosFeed

admin.autodiscover()

urlpatterns = patterns('',

    # serve static media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': MEDIA_ROOT, 'show_indexes': True}),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/photos/photo/$', 'clayto_2.photos.admin_views.change'),
    (r'^admin/', include(admin.site.urls)),

    # photos app urls
    (r'^learn/$',                           'photos.views.learn' ),
    (r'^photos/$',                          'photos.views.photos' ),
    (r'^photos/(?P<_page_number>.*)$',      'photos.views.photos' ),
    (r'^photo/(?P<photo_number>.*)$',       'photos.views.photo' ),
    (r'^$', 'photos.views.index' ),

    # feeds
    (r'^feeds/rss/$',  RssPhotosFeed() ),
    (r'^feeds/atom/$', AtomPhotosFeed() ),
    
)
