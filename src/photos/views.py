from django.shortcuts import render_to_response
from photos.models import Photo

def index( request ):
    new_photo = Photo.objects.all()[0]
    params = {
                'new_photo'  : new_photo,
                'bg_color'   : new_photo.palette0,
                'text_color' : new_photo.palette1,
                'photo_title': new_photo.title,
             }
    return render_to_response( 'index.html', params )

def photo( request, photo_slug ):
    the_photo = Photo.objects.get( slug = photo_slug )
    params = {
                'photo_file' : the_photo.image.url,
                'bg_color'   : the_photo.palette0,
                'text_color' : the_photo.palette1,
                'photo_name' : the_photo.title,
                'palette0'   : the_photo.palette0,
                'palette1'   : the_photo.palette1,
                'palette2'   : the_photo.palette2,
                'palette3'   : the_photo.palette3,
                'palette4'   : the_photo.palette4,
                'palette5'   : the_photo.palette5,
                'palette6'   : the_photo.palette6,
                'palette7'   : the_photo.palette7,
             }
    return render_to_response( 'photo.html', params )






