from src.photos.models import PhotoPost, PhotoImage
from src.photos.forms  import PhotoPostForm, PhotoImageForm
from django.db import models
from django.contrib import admin
from custom_widgets import AdminImageWidget

class PhotoPostAdmin( admin.ModelAdmin ):

    form                 = PhotoPostForm
    date_hierarchy       = 'post_date'
    prepopulated_fields  = { 'slug' : ( 'title',) }

class PhotoImageAdmin( admin.ModelAdmin ):

    form                 = PhotoImageForm
    date_hierarchy       = 'shot_date'

admin.site.register( PhotoPost, PhotoPostAdmin )
admin.site.register( PhotoImage, PhotoImageAdmin )
