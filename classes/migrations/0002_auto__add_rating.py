# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Rating'
        db.create_table('classes_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Assignment'], null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('classes', ['Rating'])

        # Adding M2M table for field ratings on 'Assignment'
        db.create_table('classes_assignment_ratings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('assignment', models.ForeignKey(orm['classes.assignment'], null=False)),
            ('rating', models.ForeignKey(orm['classes.rating'], null=False))
        ))
        db.create_unique('classes_assignment_ratings', ['assignment_id', 'rating_id'])


    def backwards(self, orm):
        
        # Deleting model 'Rating'
        db.delete_table('classes_rating')

        # Removing M2M table for field ratings on 'Assignment'
        db.delete_table('classes_assignment_ratings')


    models = {
        'classes.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'classzy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Class']", 'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'homework': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Assignment'", 'max_length': '100'}),
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
