from photos.models import Photo
from photos.forms  import PhotoAddForm, PhotoChangeForm
from django.db import models
from django.contrib import admin

class PhotoAdmin( admin.ModelAdmin ):

    add_form            = PhotoAddForm
    form                = PhotoChangeForm
    date_hierarchy      = 'post_date'
    prepopulated_fields = { 'slug' : ( 'title',) }

    #add_form_template    = "admin/photos/photopost/add_form.html"
    #change_form_template = "admin/photos/photopost/change_form.html"

    # copied from the UserAdmin in django/contrib/auth/admin.py
    def get_form( self, request, obj=None, **kwargs ):
        """
        Use special form during photo creation, instead of using the change form for
        both creation and editing.
        """
        defaults = {}
        if obj is None:
            defaults.update( {
                'form' : self.add_form,
            } )
        defaults.update( kwargs )
        return super( PhotoAdmin, self ).get_form( request, obj, **defaults )

    # copied from the UserAdmin in django/contrib/auth/admin.py
    def response_add(self, request, obj, post_url_continue='../%s/'):
        """
        Determines the HttpResponse for the add_view stage. It mostly defers to
        its superclass implementation but is customized because the User model
        has a slightly different workflow.
        """
        # setting POST['_continue'] = 1 no matter what invalidates the "save and add another"
        # and "Save" buttons, making them both act like "save and continue editing
        request.POST['_continue'] = 1
        return super(PhotoAdmin, self).response_add(request, obj, post_url_continue)


admin.site.register( Photo, PhotoAdmin )
