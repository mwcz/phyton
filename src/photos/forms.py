import django.forms as forms
from src.photos.models import Photo
from src.photos.cs import palette
from src.settings import IMAGE_SIZE_BOUNDS, MEDIA_ROOT
from custom_widgets import *
from PIL import Image

class PhotoAddForm( forms.ModelForm ):

    #slug = forms.CharField(  label = 'SLUG',  widget = AdminSlugWidget )

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

        print(m.palette0)
        print(m.palette1)
        print(m.palette2)
        print(m.palette3)
        print(m.palette4)
        print(m.palette5)
        print(m.palette6)
        print(m.palette7)

        # resize the image
        # image resizing on hold until I can figure out 
        #img_path = "%sphotos/%s/%s" % ( MEDIA_ROOT, m.slug, m.image )
        #img = img.resize( IMAGE_SIZE_BOUNDS )
        #print( img.size )
        #img.save( img_path )

        if commit:
            m.save()

        return m

    class Meta:
        model  = Photo
        fields = ("title","image","slug","shot_date",)



class PhotoChangeForm( forms.ModelForm ):

    #slug          = forms.CharField(  label = 'SLUG',  widget = AdminSlugWidget )
    #text          = forms.CharField(  label = 'TEXT' )
    #caption       = forms.CharField(  label = 'CAPT' )

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

    image         = forms.ImageField( label = 'PHOTO', widget = AdminImageWidget )
#    title         = forms.CharField(  label = 'TITLE', widget = AdminTitleWidget )
#    slug          = forms.CharField(  label = 'SLUG',  widget = AdminSlugWidget )
#    text          = forms.CharField(  label = 'TEXT',  widget = AdminTextWidget )
#    caption       = forms.CharField(  label = 'CAPT',  widget = AdminCaptionWidget )
#
#    stroke_color  = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    border_color  = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    title_color   = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    nav_color     = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    caption_color = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    post_color    = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#
#    #shot_date     = forms.CharField(  label = 'SHOT',  widget = AdminShotDateWidget )
#    palette0      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    palette1      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    palette2      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    palette3      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    palette4      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    palette5      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    palette6      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
#    palette7      = forms.CharField(  label = '',      widget = AdminSwatchWidget )

    def save(self, force_insert=False, force_update=False, commit=True):

        m = super(PhotoChangeForm, self).save(commit=False)

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

        print(m.palette0)
        print(m.palette1)
        print(m.palette2)
        print(m.palette3)
        print(m.palette4)
        print(m.palette5)
        print(m.palette6)
        print(m.palette7)

        # resize the image
        # image resizing on hold until I can figure out 
        #img_path = "%sphotos/%s/%s" % ( MEDIA_ROOT, m.slug, m.image )
        #img = img.resize( IMAGE_SIZE_BOUNDS )
        #print( img.size )
        #img.save( img_path )

        if commit:
            m.save()

        return m


    class Meta:
        model  = Photo
        fields = (
            "title",
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
            "slug",
            "shot_date",
            )


