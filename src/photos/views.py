from django.shortcuts import render_to_response
from django.core.paginator import *
from django.views.defaults import *
from django.http import Http404
from photos.models import Photo
from datetime import date
from settings import PROJECT_TITLE

def index( request ):
    new_photo_number = Photo.objects.filter( published = True ).count()
    return photo( request, new_photo_number )

def photos( request, _page_number=1 ):

    all_photos = Photo.objects.filter( published = True ).order_by( 'post_date', 'pk' )
    p = Paginator( all_photos, 12 )

    try:
        page = p.page( _page_number )
        new_photo = page.object_list[0]
    except ( EmptyPage ):
        # return 404 if page doesn't exist or is not an int
        raise Http404

    print(dir(page))

    params = {
                'project_title' : PROJECT_TITLE,

                # photo-related text
                'photoset': page,

                # prev/next stuff
                'has_prev' : page.has_previous(),
                'has_next' : page.has_next(),
                'prev_num' : page.previous_page_number(),
                'next_num' : page.next_page_number(),
                'num_pages': p.num_pages,
                'page_num' : _page_number,

                # colors
                'bg_color'     : '38393f',
                'text_color'   : 'fafafa',
                'border_color' : '91949b',
                'shadow_color' : '000',
                'quote_color'  : '',
                'title_color'  : 'ededef',
                'palette6'     : '',
                'palette7'     : '',
    }


    return render_to_response( 'photos.html', params )

def photo( request, photo_number=1 ):

    all_photos = Photo.objects.filter( published = True ).order_by( 'post_date' )
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

                # photo-related data
                'photo_width' : new_photo.image.width,
                'photo_height' : new_photo.image.height,

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

def learn( request ):

    params = {
                'project_title' : PROJECT_TITLE,

                # colors
                'bg_color'     : '38393f',
                'text_color'   : 'fafafa',
                'border_color' : '91949b',
                'shadow_color' : '000',
                'shadow_R'     : '0',
                'shadow_G'     : '0',
                'shadow_B'     : '0',
                'quote_color'  : '',
                'title_color'  : 'ededef',
                'palette6'     : '',
                'palette7'     : '',
    }


    return render_to_response( 'learn.html', params )


