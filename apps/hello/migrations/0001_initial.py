# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'hello_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sur_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bio', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=500)),
            ('birth_date', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=100)),
            ('contacts', self.gf('django.db.models.fields.CharField')(default='{}', max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(default='no-img.jpg', max_length=100)),
        ))
        db.send_create_signal(u'hello', ['Person'])

        # Adding model 'Request'
        db.create_table(u'hello_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=100)),
            ('body', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=500)),
            ('path', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=100)),
            ('method', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['Request'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'hello_person')

        # Deleting model 'Request'
        db.delete_table(u'hello_request')


    models = {
        u'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '500'}),
            'birth_date': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '100'}),
            'contacts': ('django.db.models.fields.CharField', [], {'default': "'{}'", 'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "'no-img.jpg'", 'max_length': '100'}),
            'sur_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hello.request': {
            'Meta': {'object_name': 'Request'},
            'body': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '500'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '100'}),
            'path': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '100'}),
            'scheme': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '100'})
        }
    }

    complete_apps = ['hello']