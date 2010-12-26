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
                    <!--<img style="width: 400px;" src="%s" /> <br />-->
    <div id="preview">

      <div id="image">
        <canvas id="stroke_tl"> The CANVAS element in HTML5 is not supported by your browser, but is required by clayto.org.</canvas>
        <canvas id="stroke_tr"> The CANVAS element in HTML5 is not supported by your browser, but is required by clayto.</canvas>
        <canvas id="photograph">The CANVAS element in HTML5 is not supported by your browser, but is required by clayto.</canvas>
      </div> <!-- /#image -->

      <div id="textuals">

          <div id="nav">
            <a href="#" class="nav" title="Previous" id="prev">-</a>
            <a href="#" class="nav" title="Gallery"  id="all" >*</a>
            <a href="#" class="nav" title="Next"     id="next">+</a>
          </div> <!-- /#nav -->

          <h2 id="title">Hands</h2>

          <div id="post">

            <blockquote id="caption">what no one could figure out.</blockquote>

            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tempor ligula eu 
                magna dictum mollis. Quisque ac interdum libero. Phasellus laoreet est quis dolor 
                imperdiet nec porta augue auctor. Nulla semper viverra odio id mattis. Phasellus et 
                tortor nec justo egestas vulputate. Pellentesque habitant morbi tristique senectus 
                et netus et malesuada fames ac turpis egestas. Sed massa mi, viverra ac condimentum 
                nec, pulvinar vitae felis. Vestibulum eget enim id elit cursus interdum.
            </p>

          </div> <!-- /#post -->

        </div> <!-- /#textuals -->

    </div> <!-- /#preview -->

                """ % value.url )

        output.append(super(AdminImageWidget, self).render(name,value,attrs))

        return mark_safe(u''.join(output))

class AdminSwatchWidget( forms.TextInput ):

    """
    An ImageField widget that shows a square colored swatch.
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

