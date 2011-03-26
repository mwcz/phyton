from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from photos.models import Photo
import datetime

# generic feed
class PhotosFeed( Feed ):

    title       = "clayto.com photo feed"
    link        = "/feed/"
    description = "a new photo each monday, wednesday, and friday"

    def items( self ):
        s = list( Photo.objects.filter( published = True ).order_by( 'post_date', 'pk' ) )
        return s[ len(s) - 12:] # only the 12 latest photos

    def item_title( self, item ):
        return item.title

    def item_description( self, item ):
        return item.title

    def item_pubdate( self, item ):
        return datetime.datetime.combine( item.post_date, datetime.time() )

    author_name = 'Michael Clayton'
    author_url  = 'http://clayto.com/'
    feed_copyright = 'Copyright (c) 2003-2011 Michael Clayton.  License: <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons BY-NC-SA 3.0</a>'
    ttl = 1440 # one day worth of minutes

class RssPhotosFeed( PhotosFeed ):
    feed_type = Rss201rev2Feed
    subtitle  = PhotosFeed.description

class AtomPhotosFeed( PhotosFeed ):
    feed_type = Atom1Feed
    subtitle  = PhotosFeed.description
