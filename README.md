Phyton
======

Phyton is a photoblogging software written in Python and powered by Django.
The "killer feature", if you could call it that, is dynamic color scheme for
each image.  Examples:

![Photograph titled X10-0](http://mwcz.org/img/sample-x10-0.png)
![Photograph titled more-water](http://mwcz.org/img/sample-more-water.png)

This branch, `revamp-2012`, is a development branch focused on a redesign,
added features, and some dependency changes.  The primary dependency change
will be adopting [ColorPal](/mwcz/ColorPal) and dropping numpy and scipy,
which are currently used to generate dynamic palettes.

Phyton was created to run my personal photography site,
[clayto.com](http://clayto.com/), and doesn't include the type of
customizability or modularity you might be expecting!

If you require extra features, feel free to hack on it.  If you have any
questions, feel free to contact me!

* @mwcz
* [mwc@clayto.com](mailto:mwc@clayto.com)
