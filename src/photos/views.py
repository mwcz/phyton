from django.shortcuts import render_to_response
from django.core.paginator import *
from django.views.defaults import *
from django.http import Http404
from photos.models import Photo
from datetime import date
from settings import PROJECT_TITLE

DEFAULT_PARAMS = {
    # project title
    'project_title'  : PROJECT_TITLE,

    # default colors
    'bg_color'       : '38393f',
    'text_color'     : 'fafafa',
    'border_color'   : '91949b',
    'shadow_color'   : '000000',
    'quote_color'    : 'fafafa',
    'title_color'    : 'ededef',
    'palette6'       : 'ededef',
    'palette7'       : 'ededef',
}

def index( request ):
    latest_photo = list( Photo.objects.filter( published = True ).order_by( 'post_date', 'pk' ) )[-1]
    return photo( request, photo_slug = latest_photo.slug )

def photos( request, _page_number=1 ):

    all_photos = Photo.objects.filter( published = True ).order_by( 'post_date', 'pk' )
    p = Paginator( all_photos, 12 )

    try:
        page = p.page( _page_number )
        new_photo = page.object_list[0]
    except ( EmptyPage ):
        # return 404 if page doesn't exist or is not an int
        raise Http404

    params = DEFAULT_PARAMS.copy()

    # photo-related text
    params['photoset']  = page

    # prev/next stuff
    params['has_prev']  = page.has_previous()
    params['has_next']  = page.has_next()
    params['prev_num']  = page.previous_page_number()
    params['next_num']  = page.next_page_number()
    params['num_pages'] = p.num_pages
    params['page_num']  = _page_number

	# colors
    params['shadow_R'] = 0
    params['shadow_G'] = 0
    params['shadow_B'] = 0

    return render_to_response( 'photos.html', params )



def photo( request, **kwargs ):

    all_photos = list( Photo.objects.filter( published = True ).order_by( 'post_date', 'pk' ) )
    p = Paginator( all_photos, 1 )

    if 'photo_permalink' in kwargs:
        this_photo = Photo.objects.filter( published = True ).get( permalink = kwargs['photo_permalink'] )
        photo_number = all_photos.index( this_photo) + 1
    elif 'photo_slug' in kwargs:
        this_photo = Photo.objects.filter( published = True ).get( slug = kwargs['photo_slug'] )
        photo_number = all_photos.index( this_photo ) + 1
    else:
        this_photo = all_photos[0]
        photo_number = count( all_photos ) 

    try:
        this_page  = p.page( photo_number )
    except ( PageNotAnInteger, EmptyPage ):
        # return 404 if page doesn't exist or is not an int
        raise Http404

    # build (R,G,B) shadow color.  can't use hex encoding since
    # the R,G,B values must be placed into an rgba(R,G,B,A) CSS3
    # string.
    shadow_color = (
        int( this_photo.palette2[0:2], 16 ),
        int( this_photo.palette2[2:4], 16 ),
        int( this_photo.palette2[4:6], 16 ),
    )

    params = DEFAULT_PARAMS.copy()

    # prev/next stuff
    params['this_photo']    = this_photo

    if this_page.has_previous():
        params['prev_photo']    = p.page( int(photo_number) - 1 ).object_list[0]
    if this_page.has_next():
        params['next_photo']    = p.page( int(photo_number) + 1 ).object_list[0]

    # colors
    params['bg_color']      = this_photo.palette0[:6]
    params['text_color']    = this_photo.palette1[:6]
    params['shadow_R']      = shadow_color[0]
    params['shadow_G']      = shadow_color[1]
    params['shadow_B']      = shadow_color[2]
    params['border_color']  = this_photo.palette3[:6]
    params['quote_color']   = this_photo.palette4[:6]
    params['title_color']   = this_photo.palette5[:6]
    params['palette6']      = this_photo.palette6[:6]
    params['palette7']      = this_photo.palette7[:6]

    return render_to_response( 'photo.html', params )

def learn( request ):

    params = DEFAULT_PARAMS.copy()

    # colors
    params['shadow_R'] = 0
    params['shadow_G'] = 0
    params['shadow_B'] = 0

    return render_to_response( 'learn.html', params )


