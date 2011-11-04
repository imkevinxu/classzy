# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Assignment'
        db.create_table('classes_assignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classzy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Class'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('homework', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('test', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('classes', ['Assignment'])

        # Deleting field 'Class.professor'
        db.delete_column('classes_class', 'professor')

        # Adding field 'Class.views'
        db.add_column('classes_class', 'views', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding M2M table for field assigments on 'Class'
        db.create_table('classes_class_assigments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['classes.class'], null=False)),
            ('assignment', models.ForeignKey(orm['classes.assignment'], null=False))
        ))
        db.create_unique('classes_class_assigments', ['class_id', 'assignment_id'])


    def backwards(self, orm):
        
        # Deleting model 'Assignment'
        db.delete_table('classes_assignment')

        # Adding field 'Class.professor'
        db.add_column('classes_class', 'professor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Class.views'
        db.delete_column('classes_class', 'views')

        # Removing M2M table for field assigments on 'Class'
        db.delete_table('classes_class_assigments')


    models = {
        'classes.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'classzy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classes.Class']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'homework': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'classes.class': {
            'Meta': {'object_name': 'Class'},
            'assigments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Class_Assignments'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['classes.Assignment']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['classes']
