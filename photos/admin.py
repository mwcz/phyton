from clayto_2.photos.models import Photo
from clayto_2.photos.forms  import PhotoForm
from django.contrib import admin
from custom_widgets import AdminImageWidget

class PhotoAdmin( admin.ModelAdmin ):

    form                 = PhotoForm
    add_form_template    = 'admin/photos/add_form.html'
    change_form_template = 'admin/photos/change_form.html'
    date_hierarchy       = 'post_date'
    exclude              = ('slug',)

    def formfield_for_dbfield( self, db_field, **kwargs ):
        if db_field.name == 'image':
            kwargs['widget'] = AdminImageWidget
            print( kwargs )
            print( "db_field.name == 'image'" )
        else:
            print( "db_field.name != 'image'" )
        return super( PhotoAdmin, self ).formfield_for_dbfield( db_field, **kwargs )

admin.site.register( Photo, PhotoAdmin )
