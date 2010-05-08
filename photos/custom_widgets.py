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

        output = []

        if value and hasattr(value, "url"):
            output.append('<img width="" style="position: absolute; top: 0; left: 0;" src="%s" /> <br />' % value.url )

        output.append(super(AdminImageWidget, self).render(name,value,attrs))

        return mark_safe(u''.join(output))

class AdminSwatchWidget( forms.TextInput ):

    """
    An ImageField widget that shows the current image.
    """

    def __init__(self, attrs={}):
        super( AdminSwatchWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        output.append( 
            """<span style="clear: both; padding: 0; margin: 3px; background-color: rgb%s; float: left; width: 55px; height: 55px; display: block;">&nbsp;</span>""" % value )
        output.append( 
            """<input type="hidden" name="%s" value="%s" id="id_%s" />""" % ( name, value, name ) )

        return mark_safe(u''.join(output))

