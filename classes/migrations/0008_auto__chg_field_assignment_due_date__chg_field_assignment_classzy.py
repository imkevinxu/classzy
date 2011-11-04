# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Assignment.due_date'
        db.alter_column('classes_assignment', 'due_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Assignment.classzy'
        db.alter_column('classes_assignment', 'classzy_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Class'], null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Assignment.due_date'
        raise RuntimeError("Cannot reverse this migration. 'Assignment.due_date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Assignment.classzy'
        raise RuntimeError("Cannot reverse this migration. 'Assignment.classzy' and its values cannot be restored.")


    models = {
        'classes.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'classzy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Class']", 'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'homework': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Assignment'", 'max_length': '100'}),
            'test': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'classes.class': {
            'Meta': {'object_name': 'Class'},
            'assignments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Class_Assignments'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Assignment']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['classes']
