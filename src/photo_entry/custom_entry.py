from django.db import models
from zinnia.models import EntryAbstractClass
from palette.models import Palette
from photo.models import Photo

class PhotoEntry( EntryAbstractClass ):

    photo   = models.ForeignKey( Photo, related_name='entry' )
    palette = models.ForeignKey( Palette, related_name='entry' )

    class Meta:
        abstract = True


