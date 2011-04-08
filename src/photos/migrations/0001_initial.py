# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('photos_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('permalink', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('mod_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('post_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('shot_date', self.gf('django.db.models.fields.DateField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('palette0', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('palette1', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('palette2', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('palette3', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('palette4', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('palette5', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('palette6', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('palette7', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('suggest0', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('suggest1', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('suggest2', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('suggest3', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('suggest4', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('suggest5', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('suggest6', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('suggest7', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
        ))
        db.send_create_signal('photos', ['Photo'])


    def backwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('photos_photo')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['photos']
