from clayto_2.photos.models import Photo
from django.contrib import admin
from photos.forms import PhotoForm

class PhotoAdmin( admin.ModelAdmin ):
    add_form_template    = 'admin/photos/add_form.html'
    change_form_template = 'admin/photos/change_form.html'
    date_hierarchy       = 'post_date'
    exclude              = ('slug',)
    #form                 = PhotoForm

admin.site.register( Photo, PhotoAdmin )
print("REGISTEREd")
