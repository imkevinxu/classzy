# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Time'
        db.create_table('classes_time', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Assignment'], null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('classes', ['Time'])

        # Adding field 'Assignment.num_times'
        db.add_column('classes_assignment', 'num_times', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding M2M table for field times on 'Assignment'
        db.create_table('classes_assignment_times', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('assignment', models.ForeignKey(orm['classes.assignment'], null=False)),
            ('time', models.ForeignKey(orm['classes.time'], null=False))
        ))
        db.create_unique('classes_assignment_times', ['assignment_id', 'time_id'])


    def backwards(self, orm):
        
        # Deleting model 'Time'
        db.delete_table('classes_time')

        # Deleting field 'Assignment.num_times'
        db.delete_column('classes_assignment', 'num_times')

        # Removing M2M table for field times on 'Assignment'
        db.delete_table('classes_assignment_times')


    models = {
        'classes.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'avg_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'classzy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Class']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Assignments_Comments'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Comment']"}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'homework': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_comment_name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'latest_comment_text': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Assignment'", 'max_length': '100'}),
            'num_ratings': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_times': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ratings': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Assignments_Ratings'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Rating']"}),
            'test': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'times': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Assignments_Times'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Time']"})
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
        'classes.comment': {
            'Meta': {'object_name': 'Comment'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Assignment']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
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
