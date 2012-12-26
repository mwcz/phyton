import os
from django import forms
from photos.models import Photo
from settings import IMAGE_SIZE_BOUNDS, MEDIA_ROOT
from custom_widgets import *
from PIL import Image

class PhotoAddForm( forms.ModelForm ):

    class Meta:
        model  = Photo
        fields = ('image','title','slug','shot_date','post_date')



class PhotoChangeForm( PhotoAddForm ):

    image = forms.ImageField( label = 'PHOTO', widget = AdminImageWidget )

    palette0 =   forms.CharField(  label = '',   widget = AdminEditableSwatchWidget )
    palette1 =   forms.CharField(  label = '',   widget = AdminEditableSwatchWidget )
    palette2 =   forms.CharField(  label = '',   widget = AdminEditableSwatchWidget )
    palette3 =   forms.CharField(  label = '',   widget = AdminEditableSwatchWidget )
    palette4 =   forms.CharField(  label = '',   widget = AdminEditableSwatchWidget )
    palette5 =   forms.CharField(  label = '',   widget = AdminEditableSwatchWidget )
    palette6 =   forms.CharField(  label = '',   widget = AdminEditableSwatchWidget )
    palette7 =   forms.CharField(  label = '',   widget = AdminEditableSwatchWidget )

    suggest0 =   forms.CharField(  label = '',   widget = AdminGeneratedSwatchWidget )
    suggest1 =   forms.CharField(  label = '',   widget = AdminGeneratedSwatchWidget )
    suggest2 =   forms.CharField(  label = '',   widget = AdminGeneratedSwatchWidget )
    suggest3 =   forms.CharField(  label = '',   widget = AdminGeneratedSwatchWidget )
    suggest4 =   forms.CharField(  label = '',   widget = AdminGeneratedSwatchWidget )
    suggest5 =   forms.CharField(  label = '',   widget = AdminGeneratedSwatchWidget )
    suggest6 =   forms.CharField(  label = '',   widget = AdminGeneratedSwatchWidget )
    suggest7 =   forms.CharField(  label = '',   widget = AdminGeneratedSwatchWidget )

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
            )


