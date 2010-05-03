from clayto_2.photos.models import Photo
from clayto_2.photos.forms  import PhotoForm
from django.db import models
from django.contrib import admin
from custom_widgets import AdminImageWidget

class PhotoAdmin( admin.ModelAdmin ):

    form                 = PhotoForm
    #add_form_template    = 'admin/photos/add_form.html'
    #change_form_template = 'admin/photos/change_form.html'
    date_hierarchy       = 'post_date'
    exclude              = ('slug',)
    #formfield_overrides  = { models.ImageField : { 'widget' : AdminImageWidget }, }

admin.site.register( Photo, PhotoAdmin )
