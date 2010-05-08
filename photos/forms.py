import django.forms as forms
from clayto_2.photos.models import Photo
from clayto_2.photos.cs import palette
from clayto_2.settings import IMAGE_SIZE_BOUNDS, MEDIA_ROOT
from custom_widgets import AdminImageWidget, AdminSwatchWidget
from PIL import Image

class PhotoForm( forms.ModelForm ):

    image         = forms.ImageField( label = 'PHOTO', widget = AdminImageWidget )
    stroke_color  = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    border_color  = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    title_color   = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    nav_color     = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    caption_color = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    post_color    = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    palette0      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    palette1      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    palette2      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    palette3      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    palette4      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    palette5      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    palette6      = forms.CharField(  label = '',      widget = AdminSwatchWidget )
    palette7      = forms.CharField(  label = '',      widget = AdminSwatchWidget )

    class Meta:
        model = Photo

    def save(self, force_insert=False, force_update=False, commit=True):

        m = super(PhotoForm, self).save(commit=False)

        # get the image's palette
        p = palette( m.image, 8 )
        m.palette0, m.palette1, m.palette2, m.palette3, m.palette4, m.palette5, m.palette6, m.palette7 = p

        # resize the image
        img_path = "%sphotos/%s/%s" % ( MEDIA_ROOT, m.slug, m.image )
        print( img_path )
        img = Image.open( img_path )
        img = img.resize( IMAGE_SIZE_BOUNDS )
        img.save( img_path )

        if commit:
            m.save()

        return m
