from clayto_2.photos.models import Photo
from clayto_2.photos.forms  import PhotoForm
from django.db import models
from django.contrib import admin
from custom_widgets import AdminImageWidget

class PhotoAdmin( admin.ModelAdmin ):

    form                 = PhotoForm
    date_hierarchy       = 'post_date'
    prepopulated_fields  = { 'slug' : ( 'title',) }

admin.site.register( Photo, PhotoAdmin )
