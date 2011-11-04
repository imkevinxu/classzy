# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Class.professor'
        db.add_column('classes_class', 'professor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Class.professor'
        db.delete_column('classes_class', 'professor')


    models = {
        'classes.class': {
            'Meta': {'object_name': 'Class'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['classes']
