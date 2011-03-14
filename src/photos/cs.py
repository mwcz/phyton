#!/usr/bin/python

from PIL import Image, ImageChops

def palette( _image, _size ):

    #IMAGE_FILE    = _image     # path to image file
    NODES         = _size      # how many swatches the palette will have
    IMAGE         = _image.convert("RGB")
    IMAGE_REDUCED = IMAGE.convert( "P", palette = Image.ADAPTIVE, colors = NODES ).convert("RGB")

    colors = {}
    palette = []

    for (r,g,b) in IMAGE_REDUCED.getdata():
        colors[ (r,g,b) ] = 1

    for (r,g,b) in colors:
        palette.append( "%.2x%.2x%.2x" % ( r, g, b ) )

    return tuple( palette )
