from django.forms import ModelForm, ImageField
from clayto_2.photos.models import Photo
from clayto_2.photos.cs import palette
from custom_widgets import AdminImageWidget

class PhotoForm( ModelForm ):

    image    = ImageField( label = 'PHOTO', widget = AdminImageWidget )

    class Meta:
        model = Photo

    def save(self, force_insert=False, force_update=False, commit=True):

        m = super(PhotoForm, self).save(commit=False)

        # do custom stuff
        p = palette( m.image, 8 )
        m.palette0, m.palette1, m.palette2, m.palette3, m.palette4, m.palette5, m.palette6, m.palette7 = p

        if commit:
            m.save()

        return m
