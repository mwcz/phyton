from django.db import models

class Photo( models.Model ):
    
    title        = models.CharField( max_length = 1024 )
    slug         = models.SlugField()
    caption      = models.CharField( max_length = 1024 )
    text         = models.TextField()

    post_date    = models.DateField( 'date posted', auto_now_add = True,  )
    shot_date    = models.DateField( 'date shot' )
    mod_date     = models.DateField( 'date modified', auto_now   = True,  )

    stripe_color = models.CharField( max_length = 6 )
    border_color = models.CharField( max_length = 6 )

    prepopulated_fields = { "slug" : ( "title", ) }
