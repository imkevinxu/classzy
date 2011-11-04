# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Class.id'
        db.delete_column('classes_class', 'id')

        # Changing field 'Class.code'
        db.alter_column('classes_class', 'code', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True))

        # Adding unique constraint on 'Class', fields ['code']
        db.create_unique('classes_class', ['code'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Class', fields ['code']
        db.delete_unique('classes_class', ['code'])

        # User chose to not deal with backwards NULL issues for 'Class.id'
        raise RuntimeError("Cannot reverse this migration. 'Class.id' and its values cannot be restored.")

        # Changing field 'Class.code'
        db.alter_column('classes_class', 'code', self.gf('django.db.models.fields.CharField')(max_length=20))


    models = {
        'classes.class': {
            'Meta': {'object_name': 'Class'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classes']
