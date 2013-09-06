# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'exams_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('docs', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('clinical_data', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'exams', ['Patient'])

        # Adding model 'ExamParams'
        db.create_table(u'exams_examparams', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modality', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dcm_dump', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'exams', ['ExamParams'])

        # Adding model 'PerfusionCT'
        db.create_table(u'exams_perfusionct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('af', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bv', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mtt', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'exams', ['PerfusionCT'])

        # Adding model 'Examination'
        db.create_table(u'exams_examination', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modality', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ce_agent', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ce_conc', self.gf('django.db.models.fields.IntegerField')()),
            ('ce_volume', self.gf('django.db.models.fields.IntegerField')()),
            ('ce_speed_suggested', self.gf('django.db.models.fields.IntegerField')()),
            ('ce_speed_real', self.gf('django.db.models.fields.IntegerField')()),
            ('ce_water_volume', self.gf('django.db.models.fields.IntegerField')()),
            ('ce_water_speed', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('conclusion', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'exams', ['Examination'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'exams_patient')

        # Deleting model 'ExamParams'
        db.delete_table(u'exams_examparams')

        # Deleting model 'PerfusionCT'
        db.delete_table(u'exams_perfusionct')

        # Deleting model 'Examination'
        db.delete_table(u'exams_examination')


    models = {
        u'exams.examination': {
            'Meta': {'object_name': 'Examination'},
            'ce_agent': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ce_conc': ('django.db.models.fields.IntegerField', [], {}),
            'ce_speed_real': ('django.db.models.fields.IntegerField', [], {}),
            'ce_speed_suggested': ('django.db.models.fields.IntegerField', [], {}),
            'ce_volume': ('django.db.models.fields.IntegerField', [], {}),
            'ce_water_speed': ('django.db.models.fields.IntegerField', [], {}),
            'ce_water_volume': ('django.db.models.fields.IntegerField', [], {}),
            'conclusion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modality': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'exams.examparams': {
            'Meta': {'object_name': 'ExamParams'},
            'dcm_dump': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modality': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exams.patient': {
            'Meta': {'object_name': 'Patient'},
            'clinical_data': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'docs': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'exams.perfusionct': {
            'Meta': {'object_name': 'PerfusionCT'},
            'af': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtt': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['exams']