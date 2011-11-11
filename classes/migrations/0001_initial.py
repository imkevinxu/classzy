# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Class'
        db.create_table('classes_class', (
            ('key', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('professor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('classes', ['Class'])

        # Adding M2M table for field assignments on 'Class'
        db.create_table('classes_class_assignments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['classes.class'], null=False)),
            ('assignment', models.ForeignKey(orm['classes.assignment'], null=False))
        ))
        db.create_unique('classes_class_assignments', ['class_id', 'assignment_id'])

        # Adding model 'Assignment'
        db.create_table('classes_assignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classzy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Class'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Assignment', max_length=100)),
            ('homework', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('test', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('classes', ['Assignment'])


    def backwards(self, orm):
        
        # Deleting model 'Class'
        db.delete_table('classes_class')

        # Removing M2M table for field assignments on 'Class'
        db.delete_table('classes_class_assignments')

        # Deleting model 'Assignment'
        db.delete_table('classes_assignment')


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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['classes']
