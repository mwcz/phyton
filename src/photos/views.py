from django.shortcuts import render_to_response
from photos.models import Photo

def index( request ):
    all_photos = Photo.objects.all()
    params = {
                'all_photos' : all_photos,
             }
    return render_to_response( 'index.html', params )

def photo( request, photo_slug ):
    print(photo_slug)
    the_photo = Photo.objects.get( slug = photo_slug )
    params = {
                'photo_file' : the_photo.image.url,
                'bg_color'   : the_photo.stroke_color,
                'photo_name' : the_photo.title,
                'palette0'   : the_photo.stroke_color,
                'palette1'   : the_photo.border_color,
                'palette2'   : the_photo.title_color,
                'palette3'   : the_photo.nav_color,
                'palette4'   : the_photo.caption_color,
                'palette5'   : the_photo.post_color,
             }
    return render_to_response( 'photos/photo.html', params )






