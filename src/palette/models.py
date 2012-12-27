from django.db import models

class Swatch( models.Model ):
	rgb = models.CharField( max_length = 6 )
    # H = models.IntegerField()
    # S = models.IntegerField()
    # L = models.IntegerField()

class Palette( models.Model ):
    swatch0 = models.ForeignKey( Swatch, related_name='palette0' )
    swatch1 = models.ForeignKey( Swatch, related_name='palette1' )
    swatch2 = models.ForeignKey( Swatch, related_name='palette2' )
    swatch3 = models.ForeignKey( Swatch, related_name='palette3' )
    swatch4 = models.ForeignKey( Swatch, related_name='palette4' )
    swatch5 = models.ForeignKey( Swatch, related_name='palette5' )
    swatch6 = models.ForeignKey( Swatch, related_name='palette6' )
    swatch7 = models.ForeignKey( Swatch, related_name='palette7' )

