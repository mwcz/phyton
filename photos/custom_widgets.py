from django import forms
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget

class AdminImageWidget( forms.FileInput ):

    """
    An ImageField widget that shows the current image.
    """

    def __init__(self, attrs={}):
        super( AdminImageWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        print( "RENDERING CUSTOM IMAGE WIDGET" )

        output = []

        if value and hasattr(value, "url"):
            output.append('%s <img src="%s" /> <br />CHANGE!!!!!' % ( value, value.url ) )

        output.append(super(AdminImageWidget, self).render(name,value,attrs))

        return mark_safe(u''.join(output))


