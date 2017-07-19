# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        from django.core.management import call_command
        call_command("loaddata", "request.json")

    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
