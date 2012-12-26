from django.core.management.base import BaseCommand, CommandError
from photos.models import Photo
from datetime import date

class Command( BaseCommand ):

    args = 'none'
    help = 'Sets published to True for any photos with a post_date on or after today.'

    def handle( self, *args, **options ):
        """Get all unpublished photos destined to be published today and publish them."""
        photos_to_publish = Photo.objects.filter( published=False, post_date__lte=date.today() )
        for photo in photos_to_publish:
            photo.published = True
            photo.save()
