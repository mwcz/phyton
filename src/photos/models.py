import os
import sys
import datetime
from hashlib import md5
from random import randint
from settings import ROOT_URL
from django.db import models
from django.forms import ModelForm
from PIL import Image
from settings import IMAGE_SIZE_BOUNDS, IMAGE_THUMBNAIL_SIZE_BOUNDS, MEDIA_ROOT
from photos.cs import palette

class Photo( models.Model ):

    def get_photo_number( self ):
        """enumerates all photos and finds the position of a given photo within that enumeration.  used when directly linking to photos."""
        return [ i for i,v in enumerate( Photo.objects.filter( published = True ).order_by( 'post_date', 'pk' ), 1 ) if v == self ][0]

    def __str__( self ):
        return self.title

    def get_absolute_url( self ):
        return '%sphoto/permalink/%s' % ( ROOT_URL, self.permalink )

    def create_thumbnail_path( self, filepath ):

        # create the file path for the thumbnail image 
        split_path = os.path.split( filepath )
        thumbnail_filename = "thumbnail_%s" % split_path[1]
        thumbnail_path = os.path.join( split_path[0], thumbnail_filename )

        return thumbnail_path


    def __path__( instance, filename ):
        path = os.path.join( 'photos', instance.slug, filename )
        return path

    def save( self, *args, **kwargs ):

        # determine if this is the first time this record has been saved BEFORE
        # the super().save() below (because that save will create the pk).
        # we need to know if it was the first save AFTER the super().save()
        first_save = False
        if not self.pk:
            first_save = True

        # save so that the image file will be uploaded
        super( Photo, self ).save( *args, **kwargs )

        img = Image.open( self.image )
        # resize the image
        photo_filename = str(self.image)
        img_path = os.path.join( MEDIA_ROOT, photo_filename )

        img_hash = md5( img.tostring() ).hexdigest()

        # resize down to the maximum size for the main image, then save
        if img.size[0] > IMAGE_SIZE_BOUNDS[0] or img.size[1] > IMAGE_SIZE_BOUNDS[1]:
            img.thumbnail( IMAGE_SIZE_BOUNDS, Image.ANTIALIAS )
            img.save( img_path, quality=95 )

        # if a new image has been uploaded
        if self.image_hash != img_hash:
            # initialize each palette color.  by default the
            # "custom palette" is the same as the "suggested palette".
            # each color is in hex RRGGBB format.
        
            # get the image's palette
            p = palette( img, 8 )
            self.suggest0 = p[0]
            self.suggest1 = p[1]
            self.suggest2 = p[2]
            self.suggest3 = p[3]
            self.suggest4 = p[4]
            self.suggest5 = p[5]
            self.suggest6 = p[6]
            self.suggest7 = p[7]

            img_hash = md5( img.tostring() ).hexdigest()

            # resize down to maximum size for thumbnails, then save
            thumbnail_rel_path = self.create_thumbnail_path( str( self.image ) )
            thumbnail_abs_path = self.create_thumbnail_path( img_path )
            img.thumbnail( IMAGE_THUMBNAIL_SIZE_BOUNDS, Image.ANTIALIAS )
            img.save( thumbnail_abs_path, quality=95 )
            self.thumbnail = thumbnail_rel_path

            # update the image hash
            self.image_hash = img_hash


        # if this is the first save...
        if first_save:
            # create a permalink by hashing the primary key and the current time (precise to microseconds on linux)
            self.permalink = md5( '%d%s' % ( randint(0,sys.maxint), datetime.datetime.now() ) ).hexdigest()

            # set the current palette to the suggested palette
            self.palette0 = self.suggest0
            self.palette1 = self.suggest1
            self.palette2 = self.suggest2
            self.palette3 = self.suggest3
            self.palette4 = self.suggest4
            self.palette5 = self.suggest5
            self.palette6 = self.suggest6
            self.palette7 = self.suggest7


        # save the record again to preserve the palette colors and thumbnail path
        super( Photo, self ).save( *args, **kwargs )


    image         = models.ImageField( upload_to = __path__ )
    thumbnail     = models.CharField( max_length = 1024 )
    image_hash    = models.CharField( max_length = 32 ) # md5 digest of the image's pixels

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
