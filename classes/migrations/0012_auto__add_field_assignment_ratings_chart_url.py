# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Assignment.ratings_chart_url'
        db.add_column('classes_assignment', 'ratings_chart_url', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Assignment.ratings_chart_url'
        db.delete_column('classes_assignment', 'ratings_chart_url')


    models = {
        'classes.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'avg_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'chart_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'classzy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Class']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Assignments_Comments'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Comment']"}),
            'delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'delete_queue': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'Assignment_Delete'", 'unique': 'True', 'null': 'True', 'to': "orm['classes.Delete_Queue']"}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'homework': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_comment_name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'latest_comment_text': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Assignment'", 'max_length': '100'}),
            'num_ratings': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_times': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ratings': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Assignments_Ratings'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Rating']"}),
            'ratings_chart_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'times': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Assignments_Times'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Time']"})
        },
        'classes.class': {
            'Meta': {'object_name': 'Class'},
            'assignments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Class_Assignments'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Assignment']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'delete_queue': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'Class_Delete'", 'unique': 'True', 'null': 'True', 'to': "orm['classes.Delete_Queue']"}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'classes.comment': {
            'Meta': {'object_name': 'Comment'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Assignment']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'classes.delete_queue': {
            'Meta': {'object_name': 'Delete_Queue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'classes.rating': {
            'Meta': {'object_name': 'Rating'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Assignment']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'classes.time': {
            'Meta': {'object_name': 'Time'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Assignment']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['classes']
