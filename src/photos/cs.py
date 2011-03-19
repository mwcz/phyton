from PIL import Image
from scipy.cluster import vq
from scipy import *
from numpy import random
from copy import deepcopy

# don't want random starting points for the kd-means centroids.
# the palette should be the same every time it's run.
# 13 was chosen arbitrarily.
random.seed( 13 )

def palette( _image, _size ):
    """Calculates the 'important' colors in an image using kd-means."""
    img = _image.copy()
    img.thumbnail( (64,64) )            # downsize the image so kd-means will run MUCH faster.

    pixels = list( img.getdata() )
    wh_pixels = vq.whiten( pixels )

    code_book, dist = vq.kmeans( wh_pixels, 8, 20, 1e-6 )
    #code_book, dist = vq.kmeans( wh_pixels, _size )

    code_ids, distortion = vq.vq( wh_pixels, code_book )

    clusters = []

    for i in range( len( code_book ) ):
        rgb =  px_avg( compress( code_ids == i, pixels, 0 ) )
        clusters.append( "%.2x%.2x%.2x" % ( rgb[0], rgb[1], rgb[2] ) )
        print(rgb,clusters[i])

    # since kd-means doesn't always find exactly _size centroids,
    # fill in any remaining centroids with black.
    if len( clusters ) < _size:
        for i in range( len( clusters ), _size+1 ):
            clusters.append( "000000" )

    return tuple( clusters )

def px_avg( _pixels ):
    """Accepts a list of RGB values in the form of [ (R0,G0,B0), (R1,G1,B1), ..., (Rn,Gn,Bn) ] and averages them into a single (R,G,B) tuple."""
    num_pixels = len( _pixels )
    r_avg = sum( [ pixel[0] for pixel in _pixels ] ) / num_pixels
    g_avg = sum( [ pixel[1] for pixel in _pixels ] ) / num_pixels
    b_avg = sum( [ pixel[2] for pixel in _pixels ] ) / num_pixels
    return ( r_avg, g_avg, b_avg )

