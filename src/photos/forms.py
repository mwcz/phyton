import django.forms as forms
from src.photos.models import Photo
from src.photos.cs import palette
from src.settings import IMAGE_SIZE_BOUNDS, MEDIA_ROOT
from custom_widgets import *
from PIL import Image

class PhotoAddForm( forms.ModelForm ):

    def save(self, force_insert=False, force_update=False, commit=True):

        m = super(PhotoAddForm, self).save(commit=False)

        # get the image's palette
        img = Image.open( m.image )
        p = palette( img, 8 )

        # save each color in "rgb(R,G,B)" format
        m.palette0 = "rgb%s" % str( p[0] )
        m.palette1 = "rgb%s" % str( p[1] )
        m.palette2 = "rgb%s" % str( p[2] )
        m.palette3 = "rgb%s" % str( p[3] )
        m.palette4 = "rgb%s" % str( p[4] )
        m.palette5 = "rgb%s" % str( p[5] )
        m.palette6 = "rgb%s" % str( p[6] )
        m.palette7 = "rgb%s" % str( p[7] )
        m.stroke_color = m.palette0
        m.border_color = m.palette1
        m.title_color = m.palette2
        m.nav_color = m.palette3
        m.caption_color = m.palette4
        m.post_color = m.palette5

        # resize the image
        img_path = "%s%s" % ( MEDIA_ROOT, m.image )
        img.thumbnail( IMAGE_SIZE_BOUNDS )
        img.save( img_path )

        if commit:
            m.save()

        return m

    class Meta:
        model  = Photo
        fields = ("title","image","slug","shot_date",)



class PhotoChangeForm( PhotoAddForm ):

    image = forms.ImageField( label = 'PHOTO', widget = AdminImageWidget )

    stroke_color  = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    border_color  = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    title_color   = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    nav_color     = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    caption_color = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    post_color    = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )

    palette0      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    palette1      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    palette2      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    palette3      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    palette4      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    palette5      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    palette6      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    palette7      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )

    def save(self, force_insert=False, force_update=False, commit=True):

        m = super(PhotoAddForm, self).save(commit=False)

        # get the image's palette
        img = Image.open( m.image )
        p = palette( img, 8 )

        # save each color in "rgb(R,G,B)" format
        m.palette0 = "rgb%s" % str( p[0] )
        m.palette1 = "rgb%s" % str( p[1] )
        m.palette2 = "rgb%s" % str( p[2] )
        m.palette3 = "rgb%s" % str( p[3] )
        m.palette4 = "rgb%s" % str( p[4] )
        m.palette5 = "rgb%s" % str( p[5] )
        m.palette6 = "rgb%s" % str( p[6] )
        m.palette7 = "rgb%s" % str( p[7] )

        # resize the image
        img_path = "%s%s" % ( MEDIA_ROOT, m.image )
        img.thumbnail( IMAGE_SIZE_BOUNDS )
        img.save( img_path )


        if commit:
            m.save()

        return m


    class Meta:
        model  = Photo
        fields = (
            "title",
            "slug",
            "shot_date",
            "image",
            "stroke_color",
            "border_color",
            "title_color",
            "nav_color",
            "caption_color",
            "post_color",
            "palette0",
            "palette1",
            "palette2",
            "palette3",
            "palette4",
            "palette5",
            "palette6",
            "palette7",
            )


