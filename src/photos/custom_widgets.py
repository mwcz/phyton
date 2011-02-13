from django import forms
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget, AdminDateWidget, AdminTextareaWidget

class AdminImageWidget( forms.FileInput ):

    """
    An ImageField widget that shows the current image.
    """

    def __init__(self, attrs={}):
        super( AdminImageWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        if value and hasattr(value, "url"):
            output.append("""

                <!-- my JS library for loading images into canvas elements (it also provides some basic image
                     editing capabilities but they will not be utilized -->
                <script type="text/javascript" src="/site_media/js/phyton.js"></script> 

                <img src="%s" class="phyton_image" />

            """ % ( value.url ) )

        output.append(super(AdminImageWidget, self).render(name,value,attrs))

        return mark_safe(u''.join(output))


class AdminGeneratedSwatchWidget( forms.TextInput ):

    """
    An ImageField widget that shows a square colored swatch.  These swatches
    are part of a palette generated automatically based on an uploaded image.
    """

    def __init__(self, attrs={}):
        super( AdminGeneratedSwatchWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        output.append( 
            """<span 
                    tabindex="1"
                    class="swatch generated_swatch"
                    onclick="
                                django.jQuery(selected_swatch).css( 'backgroundColor', django.jQuery(this).css('backgroundColor') );
                                django.jQuery('#id_' + selected_swatch_name ).attr( 'value', django.jQuery(this).css('backgroundColor') );
                            " 
                    style="clear: both; background-color: %s; float: left; width: 55px; height: 55px; display: block;">&nbsp;</span>""" % ( value ) )
        output.append( 
            """<input type="hidden" name="%s" value="%s" id="id_%s" />""" % ( name, value, name ) )

        return mark_safe(u''.join(output))


class AdminEditableSwatchWidget( forms.TextInput ):

    """
    An ImageField widget that shows a square colored swatch.  These swatches
    are editable from the admin interface.  The user clicks on the editable
    swatch to indicate that they want to change that swatch.  Then they may
    click on one of the generated swatches, which will replace the color of
    the editable swatch with that of the generated swatch they clicked on.
    """

    def __init__(self, attrs={}):
        super( AdminEditableSwatchWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        # 'palette0' is the first editable swatch that will be displayed.
        # set it as the default selected swatch
        if name == 'palette0':
            output.append(
                """
                    <script type="text/javascript">
                        var selected_swatch = django.jQuery('palette0');
                        var selected_swatch_name = 'palette0';
                    </script>
                """
            )

        output.append( 
            """<span 
                    tabindex="1"
                    class="swatch editable_swatch"
                    onclick=" selected_swatch = django.jQuery(this); selected_swatch_name='%s';" style="clear: both; background-color: %s; float: left; width: 55px; height: 55px; display: block;">&nbsp;</span>""" % ( name, value ) )
        output.append( 
            """<input type="hidden" name="%s" value="%s" id="id_%s" />""" % ( name, value, name ) )

        return mark_safe(u''.join(output))


class AdminCKEditorWidget( AdminTextareaWidget ):

    """
    A textarea upgraded to a rich text area using CKEditor.
    """

    def render( self, name, value, attrs=None):

        output = []

        output.append( 
        """
            <script type="text/javascript" src="/site_media/3rd/ckeditor/ckeditor.js"></script>
            <textarea name="%s" id="id_%s" class="ckeditor">%s</textarea>
        """ % ( name, name, value ) )

        return mark_safe(u''.join(output))
