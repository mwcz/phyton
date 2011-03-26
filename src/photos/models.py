import os
import sys
import datetime
from hashlib import md5
from random import randint
from settings import ROOT_URL
from django.db import models
from django.forms import ModelForm

class Photo( models.Model ):

    def get_photo_number( self ):
        """enumerates all photos and finds the position of a given photo within that enumeration.  used when directly linking to photos."""
        return [ i for i,v in enumerate( Photo.objects.filter( published = True ).order_by( 'post_date', 'pk' ), 1 ) if v == self ][0]

    def __str__( self ):
        return self.title

    def get_absolute_url( self ):
        return '%sphoto/permalink/%s' % ( ROOT_URL, self.permalink )

    def __path__( instance, filename ):
        try:
            os.mkdir('./photos')
            os.mkdir('./photos/%s' % instance.slug )
        except OSError:
            pass # directory already exists
        path = 'photos/%s/%s' % ( instance.slug, filename )
        return path

    def save( self, *args, **kwargs ):

        # if this is the first save, create a permalink by hashing the primary key and the
        # current time (precise to microseconds on linux)
        if not self.pk:
            self.permalink = md5( '%d%s' % ( randint(0,sys.maxint), datetime.datetime.now() ) ).hexdigest()

        super( Photo, self ).save( *args, **kwargs )

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
