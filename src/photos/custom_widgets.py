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

            """ % value.url )

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



        if name == 'suggest0':
            output.append(
                """
                    <script type="text/javascript">

                        // thanks to @fudgey on StackOverflow!
                        // this function is needed because jquery only returns rgb(R,G,B)-formatted color codes
                        // but I store 8-character RGBA values in hex
                        function rgb2hex(rgb) {

                            rgb = rgb.match(/^rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$/);

                            function hex(x) {
                                return ("0" + parseInt(x).toString(16)).slice(-2);
                            }

                            return hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);

                        }
                    </script>
                """)

        output.append( 
            """<span 
                    tabindex="1"
                    class="swatch generated_swatch"
                    onclick="
                                django.jQuery(selected_swatch).css( 'backgroundColor', django.jQuery(this).css('backgroundColor') );
                                django.jQuery('#id_' + selected_swatch_name ).attr( 'value', rgb2hex(django.jQuery(this).css('backgroundColor')) );
                            " 
                    style="clear: both; background-color: #%s; float: left; width: 55px; height: 55px; display: block;">&nbsp;</span>""" % value )
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

                    <span style="float: left;">BG</span>
                """
            )
        if name == 'palette1':
            output.append(
                """
                    <span style="float: left;">TEXT</span>
                """
            )
        if name == 'palette2':
            output.append(
                """
                    <span style="float: left;">SHADOW</span>
                """
            )
        if name == 'palette3':
            output.append(
                """
                    <span style="float: left;">BORDER</span>
                """
            )
        if name == 'palette4':
            output.append(
                """
                    <span style="float: left;">QUOTE</span>
                """
            )
        if name == 'palette5':
            output.append(
                """
                    <span style="float: left;">TITLE</span>
                """
            )
        if name == 'palette6':
            output.append(
                """
                    <span style="float: left;">UNUSED</span>
                """
            )
        if name == 'palette7':
            output.append(
                """
                    <span style="float: left;">UNUSED</span>
                """
            )
#       'bg_color' : new_photo.palette0[:6],
#       'text_color' : new_photo.palette1[:6],
#       'shadow_color' : new_photo.palette2[:6],
#       'border_color' : new_photo.palette3[:6],
#       'quote_color': new_photo.palette4[:6],
#       'title_color': new_photo.palette5[:6],
#       'palette6' : new_photo.palette6[:6],
#       'palette7' : new_photo.palette7[:6],

        output.append( 
            """<span 
                    tabindex="1"
                    class="swatch editable_swatch"
                    onclick=" selected_swatch = django.jQuery(this); selected_swatch_name='%s';" style="clear: both; background-color: #%s; float: left; width: 55px; height: 55px; display: block;">&nbsp;</span>""" % ( name, value[:6] ) )
        output.append( 
            """<input type="hidden" name="%s" value="%s" id="id_%s" />""" % ( name, value, name ) )

        return mark_safe(u''.join(output))

