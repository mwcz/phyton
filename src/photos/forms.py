from django import forms
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
        m.suggest0 = m.palette0 = "rgb%s" % str( p[0] )
        m.suggest1 = m.palette1 = "rgb%s" % str( p[1] )
        m.suggest2 = m.palette2 = "rgb%s" % str( p[2] )
        m.suggest3 = m.palette3 = "rgb%s" % str( p[3] )
        m.suggest4 = m.palette4 = "rgb%s" % str( p[4] )
        m.suggest5 = m.palette5 = "rgb%s" % str( p[5] )
        m.suggest6 = m.palette6 = "rgb%s" % str( p[6] )
        m.suggest7 = m.palette7 = "rgb%s" % str( p[7] )

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
    text  = forms.CharField( widget = AdminCKEditorWidget )

    palette0      = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    palette1      = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    palette2      = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    palette3      = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    palette4      = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    palette5      = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    palette6      = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )
    palette7      = forms.CharField(  label = '',      widget = AdminEditableSwatchWidget )

    suggest0      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    suggest1      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    suggest2      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    suggest3      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    suggest4      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    suggest5      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    suggest6      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )
    suggest7      = forms.CharField(  label = '',      widget = AdminGeneratedSwatchWidget )

    def save(self, force_insert=False, force_update=False, commit=True):

        m = super(PhotoAddForm, self).save(commit=False)

        # get the image's palette
        img = Image.open( m.image )
        p = palette( img, 8 )

        # save each color in "rgb(R,G,B)" format
        m.suggest0 = "rgb%s" % str( p[0] )
        m.suggest1 = "rgb%s" % str( p[1] )
        m.suggest2 = "rgb%s" % str( p[2] )
        m.suggest3 = "rgb%s" % str( p[3] )
        m.suggest4 = "rgb%s" % str( p[4] )
        m.suggest5 = "rgb%s" % str( p[5] )
        m.suggest6 = "rgb%s" % str( p[6] )
        m.suggest7 = "rgb%s" % str( p[7] )

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
            "text",
            "image",
            "palette0",
            "palette1",
            "palette2",
            "palette3",
            "palette4",
            "palette5",
            "palette6",
            "palette7",
            "suggest0",
            "suggest1",
            "suggest2",
            "suggest3",
            "suggest4",
            "suggest5",
            "suggest6",
            "suggest7",
            )


