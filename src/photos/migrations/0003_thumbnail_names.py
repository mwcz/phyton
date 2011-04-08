# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def create_thumbnail_path( self, filepath ):

        import os

        # create the file path for the thumbnail image 
        split_path = os.path.split( filepath )
        thumbnail_filename = "thumbnail_%s" % split_path[1]
        thumbnail_path = os.path.join( split_path[0], thumbnail_filename )

        return thumbnail_path


    def forwards(self, orm):
        "Create thumbnail paths."

        from PIL import Image
        from settings import IMAGE_THUMBNAIL_SIZE_BOUNDS, MEDIA_ROOT
        import os

        for photo in orm.Photo.objects.all():

            photo_filename = str( photo.image )
            img_path = os.path.join( MEDIA_ROOT, photo_filename )
            thumbnail_abs_path = self.create_thumbnail_path( img_path )
            thumbnail_path = self.create_thumbnail_path( photo_filename )

            img = Image.open( img_path )

            img.thumbnail( IMAGE_THUMBNAIL_SIZE_BOUNDS, Image.ANTIALIAS )
            img.save( thumbnail_abs_path )
            photo.thumbnail = thumbnail_path

            photo.save()


    def backwards(self, orm):
        "Remove thumbnail paths."

        #from PIL import Image
        from settings import IMAGE_THUMBNAIL_SIZE_BOUNDS, MEDIA_ROOT
        import os

        for photo in orm.Photo.objects.all():
            photo.thumbnail = u''
            photo.save()

            photo_filename = str( photo.image )
            img_path = os.path.join( MEDIA_ROOT, photo_filename )
            thumbnail_abs_path = self.create_thumbnail_path( img_path )

            try:
                os.remove( thumbnail_abs_path )
            except OSError:
                print( "could not remove thumbnail: %s" % thumbnail_abs_path )


    models = {
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'mod_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'palette0': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'palette1': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'palette2': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'palette3': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'palette4': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'palette5': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'palette6': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'palette7': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'post_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shot_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'suggest0': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'suggest1': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'suggest2': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'suggest3': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'suggest4': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'suggest5': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'suggest6': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'suggest7': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['photos']
