# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Photo.image_hash'
        db.add_column('photos_photo', 'image_hash', self.gf('django.db.models.fields.CharField')(default='01234567890123456789012345678901', max_length=32), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Photo.image_hash'
        db.delete_column('photos_photo', 'image_hash')


    models = {
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
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
