from django.shortcuts import render_to_response
from django.core.paginator import *
from django.views.defaults import *
from django.http import Http404
from photos.models import Photo
from settings import PROJECT_TITLE

def index( request ):
    new_photo_number = Photo.objects.count()
    return photo( request, new_photo_number )

def photos( request, _page_number=1 ):

    all_photos = Photo.objects.order_by( 'post_date' )
    p = Paginator( all_photos, 9 )

    try:
        page = p.page( _page_number )
        new_photo = page.object_list[0]
    except ( EmptyPage ):
        # return 404 if page doesn't exist or is not an int
        raise Http404

    # build (R,G,B) shadow color.  can't use hex encoding since
    # the R,G,B values must be placed into an rgba(R,G,B,A) CSS3
    # string.
    shadow_color = {
        'r' : int( new_photo.palette2[:2], 16 ),
        'g' : int( new_photo.palette2[2:4], 16 ),
        'b' : int( new_photo.palette2[4:], 16 ),
    }

    params = {
                'project_title' : PROJECT_TITLE,

                # photo-related text
                'photoset': page,

                # prev/next stuff
                'has_prev' : page.has_previous(),
                'has_next' : page.has_next(),
                'prev_num' : page.previous_page_number(),
                'next_num' : page.next_page_number(),

                # colors
                'bg_color' : new_photo.palette0,
                'text_color' : new_photo.palette1,
                'shadow_color' : shadow_color,
                'border_color' : new_photo.palette3,
                'quote_color': new_photo.palette4,
                'title_color': new_photo.palette5,
                'palette6' : new_photo.palette6,
                'palette7' : new_photo.palette7,
    }


    return render_to_response( 'photos.html', params )

def photo( request, photo_number=1 ):

    all_photos = Photo.objects.order_by( 'post_date' )
    p = Paginator( all_photos, 1 )

    try:
        page = p.page( photo_number )
        new_photo = page.object_list[0]
    except ( PageNotAnInteger, EmptyPage ):
        # return 404 if page doesn't exist or is not an int
        raise Http404

    # build (R,G,B) shadow color.  can't use hex encoding since
    # the R,G,B values must be placed into an rgba(R,G,B,A) CSS3
    # string.
    shadow_color = (
        int( new_photo.palette2[0:2], 16 ),
        int( new_photo.palette2[2:4], 16 ),
        int( new_photo.palette2[4:6], 16 ),
    )

    params = {
                'project_title' : PROJECT_TITLE,

                # photo-related text
                'photo_title': new_photo.title,
                'text': new_photo.text,

                # prev/next stuff
                'new_photo' : new_photo,
                'has_prev' : page.has_previous(),
                'has_next' : page.has_next(),
                'prev_num' : page.previous_page_number(),
                'next_num' : page.next_page_number(),

                # colors
                'bg_color' : new_photo.palette0[:6],
                'text_color' : new_photo.palette1[:6],
                'shadow_R' : shadow_color[0],
                'shadow_G' : shadow_color[1],
                'shadow_B' : shadow_color[2],
                'border_color' : new_photo.palette3[:6],
                'quote_color': new_photo.palette4[:6],
                'title_color': new_photo.palette5[:6],
                'palette6' : new_photo.palette6[:6],
                'palette7' : new_photo.palette7[:6],
             }

    return render_to_response( 'photo.html', params )

