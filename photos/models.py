from django.db import models
from django.forms import ModelForm

class Photo( models.Model ):

    def __str__( self ):
        return self.title

    def __path__( instance, filename ):
        path = 'photos/%s/%s' % ( instance.slug, filename )
        return path

    image         = models.ImageField( upload_to = __path__ )

    title         = models.CharField( max_length = 1024 )
    slug          = models.SlugField()
    caption       = models.CharField( max_length = 1024 )
    text          = models.TextField()

    shot_date     = models.DateField( 'date shot' )
    post_date     = models.DateField( 'date posted', auto_now_add = True,  )
    mod_date      = models.DateField( 'date modified', auto_now = True,  )

    stroke_color  = models.CharField( max_length = 32, blank = True )
    border_color  = models.CharField( max_length = 32, blank = True )
    title_color   = models.CharField( max_length = 32, blank = True )
    nav_color     = models.CharField( max_length = 32, blank = True )
    caption_color = models.CharField( max_length = 32, blank = True )
    post_color    = models.CharField( max_length = 32, blank = True )

    palette0 = models.CharField( max_length = 32, blank = True )
    palette1 = models.CharField( max_length = 32, blank = True )
    palette2 = models.CharField( max_length = 32, blank = True )
    palette3 = models.CharField( max_length = 32, blank = True )
    palette4 = models.CharField( max_length = 32, blank = True )
    palette5 = models.CharField( max_length = 32, blank = True )
    palette6 = models.CharField( max_length = 32, blank = True )
    palette7 = models.CharField( max_length = 32, blank = True )

