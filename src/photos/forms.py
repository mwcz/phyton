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
        m.suggest0 = m.palette0 = p[0]
        m.suggest1 = m.palette1 = p[1]
        m.suggest2 = m.palette2 = p[2]
        m.suggest3 = m.palette3 = p[3]
        m.suggest4 = m.palette4 = p[4]
        m.suggest5 = m.palette5 = p[5]
        m.suggest6 = m.palette6 = p[6]
        m.suggest7 = m.palette7 = p[7]

        # create the directory in which to place the image


        # move the image into the directory


        # resize the image
        img_path = "%s%s" % ( MEDIA_ROOT, m.image )
        img.thumbnail( IMAGE_SIZE_BOUNDS )
        img.save( img_path )

        if commit:
            m.save()

        return m

    class Meta:
        model  = Photo
        fields = ('image','title','slug','shot_date','post_date')



class PhotoChangeForm( PhotoAddForm ):

    image = forms.ImageField( label = 'PHOTO', widget = AdminImageWidget )

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
        m.suggest0 = p[0]
        m.suggest1 = p[1]
        m.suggest2 = p[2]
        m.suggest3 = p[3]
        m.suggest4 = p[4]
        m.suggest5 = p[5]
        m.suggest6 = p[6]
        m.suggest7 = p[7]

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
            "post_date",
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
            "image",
            #"text",
            )


