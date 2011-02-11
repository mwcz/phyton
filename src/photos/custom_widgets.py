from django import forms
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget, AdminDateWidget

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

        print( (name,value) )

        # 'stroke_color' is the first editable swatch that will be displayed.
        # set it as the default selected swatch
        if name == 'stroke_color':
            output.append(
                """
                    <script type="text/javascript">
                        var selected_swatch = django.jQuery('stroke_color');
                        var selected_swatch_name = 'stroke_color';
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


class AdminTitleWidget( forms.TextInput ):

    """
    An ImageField widget that shows the current image's title.
    """

    def __init__(self, attrs={}):
        super( AdminTitleWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        output.append( 
            """<input style="position: absolute; top: 272px; left: 110px;" type="text" name="%s" value="%s" id="id_%s" />
            <span style="position: absolute; top: 272px; left: 430px;">- * +</span>""" % ( name, value, name ) )

        return mark_safe(u''.join(output))


class AdminSlugWidget( forms.TextInput ):

    """
    An ImageField widget that shows the current image's title.
    """

    def __init__(self, attrs={}):
        super( AdminSlugWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        output.append( 
            """<input type="hidden" name="%s" value="%s" id="id_%s" />""" % ( name, value, name ) )

        return mark_safe(u''.join(output))


class AdminTextWidget( forms.TextInput ):

    """
    An ImageField widget that shows the current image's title.
    """

    def __init__(self, attrs={}):
        super( AdminTextWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        output.append( 
            """<textarea style="width: 395px; position: absolute; top: 335px; left: 90px;" name="%s" id="id_%s">%s</textarea>""" % ( name, name, value ) )

        return mark_safe(u''.join(output))


class AdminShotDateWidget( forms.TextInput ):

    """
    An ImageField widget that shows the current image's title.
    """

    def __init__(self, attrs={}):
        super( AdminShotDateWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        output.append( 
            """<input name="%s" value="%s" class="vDateField" type="text" id="id_%s" size="10" />""" % ( name, value, name ) )

        return mark_safe(u''.join(output))
        

class AdminCaptionWidget( forms.TextInput ):

    """
    An ImageField widget that shows the current image's title.
    """

    def __init__(self, attrs={}):
        super( AdminCaptionWidget, self).__init__(attrs)

    def render( self, name, value, attrs=None):

        output = []

        output.append( 
            """<input style="position: absolute; top: 302px; left: 214px;" type="text" name="%s" value="%s" id="id_%s" />""" % ( name, value, name ) )

        return mark_safe(u''.join(output))

