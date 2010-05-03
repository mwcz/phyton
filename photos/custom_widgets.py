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

class AdminSwatchWidget( forms.TextInput ):

    """
    An ImageField widget that shows the current image.
    """

    def __init__(self, attrs={}):
        super( AdminSwatchWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        print( "RENDERING CUSTOM SWATCH WIDGET" )
        print( name )
        print( value )
        print( attrs )

        output = []

        output.append( """<div style="background-color: rgb%s; float: left; width = 30px; height = 30px; display: block;">&nbsp;</div>""" % value )
        output.append( """<input type="hidden" name="%s" value="%s" id="id_%s" />""" % ( name, value, name ) )

        return mark_safe(u''.join(output))


