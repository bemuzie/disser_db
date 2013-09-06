# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'exams.examination': {
            'Meta': {'object_name': 'Examination'},
            'ce_agent': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ce_conc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_speed_real': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_speed_suggested': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_volume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_water_speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_water_volume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'conclusion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modality': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Patient']"})
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
    symmetrical = True
