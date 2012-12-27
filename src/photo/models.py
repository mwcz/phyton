from django.db import models
import os

class Photo( models.Model ):

    def __path__( self, filename ):
        path = os.path.join( 'photos', filename )
        return path

    image = models.ImageField( upload_to = __path__ )

