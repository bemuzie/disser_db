# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Perfusion.examination'
        db.add_column(u'exams_perfusion', 'examination',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['exams.Examination']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Perfusion.examination'
        db.delete_column(u'exams_perfusion', 'examination_id')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exams.clinicaldata': {
            'Meta': {'object_name': 'ClinicalData'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Patient']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'exams.density': {
            'Meta': {'object_name': 'Density'},
            'density': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phase': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Phase']"}),
            'roi': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'exams.docs': {
            'Meta': {'object_name': 'Docs'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Patient']"})
        },
        u'exams.examination': {
            'Meta': {'object_name': 'Examination'},
            'artefacts': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'arterial_invasion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ascit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bile_ducts_extension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ce_agent': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ce_conc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_speed_real': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_speed_suggested': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_volume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_water_speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_water_volume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'choledoch_diametr': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'distal_atrophy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lymphadenopathy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lypomatosis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'metastasis': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modality': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Patient']"}),
            'portal_invasion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'virsung_size': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'exams.patient': {
            'Meta': {'object_name': 'Patient'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'clinical_data': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'exams.perfusion': {
            'Meta': {'object_name': 'Perfusion'},
            'bf_mean': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bf_median': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bf_quantile_low': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bf_quantile_up': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bf_sd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bv_mean': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bv_median': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bv_quantile_low': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bv_quantile_up': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bv_sd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'examination': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Examination']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtt_mean': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mtt_median': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mtt_quantile_low': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mtt_quantile_up': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mtt_sd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'roi': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'roi_max_distance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'roi_size_max': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'roi_volume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ttp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'exams.perfusionct': {
            'Meta': {'object_name': 'PerfusionCT'},
            'af': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtt': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'exams.phase': {
            'Meta': {'object_name': 'Phase'},
            'examination': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Examination']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'zone': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'exams.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Patient']"}),
            'procedure': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exams.reminder': {
            'Meta': {'object_name': 'Reminder'},
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Patient']"}),
            'remind_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'exams.tagdictionary': {
            'Meta': {'object_name': 'TagDictionary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['taggit.Tag']"}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['exams']