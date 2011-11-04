# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing M2M table for field assigments on 'Class'
        db.delete_table('classes_class_assigments')

        # Adding M2M table for field assignments on 'Class'
        db.create_table('classes_class_assignments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['classes.class'], null=False)),
            ('assignment', models.ForeignKey(orm['classes.assignment'], null=False))
        ))
        db.create_unique('classes_class_assignments', ['class_id', 'assignment_id'])


    def backwards(self, orm):
        
        # Adding M2M table for field assigments on 'Class'
        db.create_table('classes_class_assigments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['classes.class'], null=False)),
            ('assignment', models.ForeignKey(orm['classes.assignment'], null=False))
        ))
        db.create_unique('classes_class_assigments', ['class_id', 'assignment_id'])

        # Removing M2M table for field assignments on 'Class'
        db.delete_table('classes_class_assignments')


    models = {
        'classes.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'classzy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Class']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
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
