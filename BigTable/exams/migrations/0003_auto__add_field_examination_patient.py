# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Examination.patient'
        db.add_column(u'exams_examination', 'patient',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['exams.Patient']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Examination.patient'
        db.delete_column(u'exams_examination', 'patient_id')


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