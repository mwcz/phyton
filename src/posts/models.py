from django.db import models
from django.forms import ModelForm
from ckeditor.fields import RichTextField

class Post( models.Model ):

    def __str__( self ):
        return self.title

    title         = models.CharField( max_length = 1024 )
    slug          = models.SlugField( unique = True )
    text          = RichTextField( blank = True )

    mod_date      = models.DateField( 'date modified', auto_now = True,  )
    post_date     = models.DateField( 'date to publish'  )
