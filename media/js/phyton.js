(function($) {
    $(document).ready( function() {

        var MODES = [ 'pixel', 'area' ];
        var current_mode = MODES[0]; // the default

        var SELECT_RECT_SIZE = [10,10]; // the width/height of the selection rectangle

        var SWATCHES = [ 
                        'div.stroke_color',
                        'div.border_color',
                        'div.title_color',
                        'div.nav_color',
                        'div.caption_color',
                        'div.post_color',
                        'div.palette0',
                        'div.palette1',
                        'div.palette2',
                        'div.palette3',
                        'div.palette4',
                        'div.palette5',
                        'div.palette6',
                        'div.palette7'
                       ];
        var current_swatch = SWATCHES[0];

        $('img.phyton_image').each( function(index) {

            // When each img.phyton_image element is done loading
            this.onload = function() {

                /**
                 * Create a canvas element.  Set its height and width to match the image's
                 * height and width.  Append it to the image's parent element, then remove
                 * the image.  This replaces the <img> with a <canvas> displaying the same
                 * image file.
                 */

                var canvas_element = document.createElement('canvas');
                var canvas_context = canvas_element.getContext('2d');
                $(canvas_element).css( 'cursor', 'http://localhost:8000/site_media/cursors/10px.cur' );

                /**
                 * img elements declared as <img src="..." /> do not have a width property.
                 * To find the width of the image we must create a temporary img element
                 * and assign it to the src of the img element in the dom.
                 */
                temp_img = new Image();
                temp_img.src = this.src;

                canvas_element.width  = this.width;
                canvas_element.height = this.height;
                canvas_element.id = 'photo';

                canvas_context.drawImage( this, 0, 0 ); // draw the image into the canvas

                // Add the canvas element to the dom and remove the img element
                // Replace the img element with the canvas element
                this.parentNode.replaceChild( canvas_element, this );


                pixel = function( e ) {

                    var x = e.pageX - canvas_element.offsetLeft;
                    var y = e.pageY - canvas_element.offsetTop;

                    var colors = canvas_context.getImageData( 
                                    x, 
                                    y,   
                                    SELECT_RECT_SIZE[0], 
                                    SELECT_RECT_SIZE[1]
                                    ).data;

                    var color = [ 0, 0, 0 ];
                    var color_count = 0;
                    // Average all the colors returned
                    for( var i = colors.length - 1; i >= 0; i-=4 ) {

                        // If there is a non-zero alpha channel
                        if( colors[i] > 0 ) {
                            ++color_count;
                            color[0] += colors[i - 3];
                            color[1] += colors[i - 2];
                            color[2] += colors[i - 1];
                        }
                    }
                    color[0] = Math.floor( color[0] / color_count );
                    color[1] = Math.floor( color[1] / color_count );
                    color[2] = Math.floor( color[2] / color_count );

                    console.log( selected_swatch_name );
                    $(selected_swatch).css( 'backgroundColor', 'rgb('+color[0]+','+color[1]+','+color[2]+')' );
                    $('#id_' + selected_swatch_name ).attr( 'value', $(selected_swatch).css('backgroundColor'));

                };

                // On mouse down, enable dragging by setting the mousemove event to pixel()
                canvas_element.onmousedown = function( e ) {
                    canvas_element.onmousemove = pixel;
                    canvas_element.onclick     = pixel;
                };

                // On mouse up, disable dragging by setting the mousemove event to null
                canvas_element.onmouseup = function() {
                    canvas_element.onmousemove = null;
                };

                // On mouse out, disable dragging by setting the mousemove event to null
                // This prevents a bug where clicking on the canvas, dragging off the canvas,
                // releasing the mouse button, and hovering over the canvas again would cause
                // pixel() to continue to fire.
                canvas_element.onmouseout = function() {
                    canvas_element.onmousemove = null;
                };

            }
            
        });

    });

})
(django.jQuery);

