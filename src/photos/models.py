import os
import sys
import datetime
from hashlib import md5
from random import randint
from settings import ROOT_URL
from django.db import models
from django.forms import ModelForm
from PIL import Image
from settings import IMAGE_SIZE_BOUNDS, MEDIA_ROOT
from photos.cs import palette

class Photo( models.Model ):

    def get_photo_number( self ):
        """enumerates all photos and finds the position of a given photo within that enumeration.  used when directly linking to photos."""
        return [ i for i,v in enumerate( Photo.objects.filter( published = True ).order_by( 'post_date', 'pk' ), 1 ) if v == self ][0]

    def __str__( self ):
        return self.title

    def get_absolute_url( self ):
        return '%sphoto/permalink/%s' % ( ROOT_URL, self.permalink )

    def __path__( instance, filename ):
        path = os.path.join( 'photos', instance.slug, filename )
        return path

    def save( self, *args, **kwargs ):

        # if this is the first save, create a permalink by hashing the primary key and the
        # current time (precise to microseconds on linux)
        if not self.pk:
            self.permalink = md5( '%d%s' % ( randint(0,sys.maxint), datetime.datetime.now() ) ).hexdigest()

        # save so that the image file will be uploaded
        super( Photo, self ).save( *args, **kwargs )

        # get the image's palette
        img = Image.open( self.image )
        p = palette( img, 8 )

        # initialize each palette color.  by default the
        # "custom palette" is the same as the "suggested palette".
        # each color is in hex RRGGBB format.
        self.suggest0 = self.palette0 = p[0]
        self.suggest1 = self.palette1 = p[1]
        self.suggest2 = self.palette2 = p[2]
        self.suggest3 = self.palette3 = p[3]
        self.suggest4 = self.palette4 = p[4]
        self.suggest5 = self.palette5 = p[5]
        self.suggest6 = self.palette6 = p[6]
        self.suggest7 = self.palette7 = p[7]

        # save the record again to preserve the palette colors
        super( Photo, self ).save( *args, **kwargs )

        # resize the image
        photo_filename = str(self.image)
        img_path = os.path.join( MEDIA_ROOT, photo_filename )
        img.thumbnail( IMAGE_SIZE_BOUNDS )
        img.save( img_path )



    image         = models.ImageField( upload_to = __path__ )

    title         = models.CharField( max_length = 1024 )
    slug          = models.SlugField( unique = True )
    caption       = models.CharField( max_length = 1024 )
    #text          = RichTextField( blank = True )
    permalink     = models.CharField( max_length = 32, editable = False )

    mod_date      = models.DateField( 'date modified', auto_now = True,  )
    post_date     = models.DateField( 'date to publish', default = datetime.date.today  )
    shot_date     = models.DateField( 'date photo was taken' )

    published     = models.BooleanField( default = False )

    # An eight-color palette for the image
    palette0 = models.CharField( max_length = 6, blank = True )
    palette1 = models.CharField( max_length = 6, blank = True )
    palette2 = models.CharField( max_length = 6, blank = True )
    palette3 = models.CharField( max_length = 6, blank = True )
    palette4 = models.CharField( max_length = 6, blank = True )
    palette5 = models.CharField( max_length = 6, blank = True )
    palette6 = models.CharField( max_length = 6, blank = True )
    palette7 = models.CharField( max_length = 6, blank = True )

    # An eight-color suggested palette generated automatically from the image
    suggest0 = models.CharField( max_length = 6, blank = True )
    suggest1 = models.CharField( max_length = 6, blank = True )
    suggest2 = models.CharField( max_length = 6, blank = True )
    suggest3 = models.CharField( max_length = 6, blank = True )
    suggest4 = models.CharField( max_length = 6, blank = True )
    suggest5 = models.CharField( max_length = 6, blank = True )
    suggest6 = models.CharField( max_length = 6, blank = True )
    suggest7 = models.CharField( max_length = 6, blank = True )
