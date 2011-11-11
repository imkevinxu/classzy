# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Assignment.num_ratings'
        db.add_column('classes_assignment', 'num_ratings', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Assignment.num_ratings'
        db.delete_column('classes_assignment', 'num_ratings')


    models = {
        'classes.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'avg_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'classzy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Class']", 'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'homework': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Assignment'", 'max_length': '100'}),
            'num_ratings': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ratings': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Assignments_Ratings'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Rating']"}),
            'test': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'classes.class': {
            'Meta': {'object_name': 'Class'},
            'assignments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Class_Assignments'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Assignment']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'classes.rating': {
            'Meta': {'object_name': 'Rating'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Assignment']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['classes']
