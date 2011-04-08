"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Photo
import os
from settings import MEDIA_ROOT

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

class ImageTests( TestCase ):

    def test_image_palette(self):
        """
        Test images uploading to the correct location.
        """

        IMAGE_FILE = "test_images/22.jpg"
        p = Photo()
        p.image = IMAGE_FILE
        p.shot_date="2010-10-10"
        p.save()

        # are the palette colors correct?
        # this test will break when/if the palette generation
        # algorithm is changed, obviously.
        self.failUnlessEqual( p.suggest0, "262624" )
        self.failUnlessEqual( p.suggest1, "797a7a" )
        self.failUnlessEqual( p.suggest2, "373835" )
        self.failUnlessEqual( p.suggest3, "111210" )
        self.failUnlessEqual( p.suggest4, "525251" )
        self.failUnlessEqual( p.suggest5, "090908" )
        self.failUnlessEqual( p.suggest6, "1a1b19" )
        self.failUnlessEqual( p.suggest7, "bbb8b3" )


__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

