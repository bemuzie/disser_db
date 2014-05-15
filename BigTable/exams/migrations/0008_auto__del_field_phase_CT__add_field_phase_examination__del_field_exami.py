# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Phase.CT'
        db.delete_column(u'exams_phase', 'CT_id')

        # Adding field 'Phase.examination'
        db.add_column(u'exams_phase', 'examination',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['exams.Examination']),
                      keep_default=False)

        # Deleting field 'Examination.act'
        db.delete_column(u'exams_examination', 'act')

        # Deleting field 'Examination.conclusion'
        db.delete_column(u'exams_examination', 'conclusion')

        # Adding field 'Examination.artefacts'
        db.add_column(u'exams_examination', 'artefacts',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True),
                      keep_default=False)

        # Adding field 'Examination.tumor_size_x'
        db.add_column(u'exams_examination', 'tumor_size_x',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Examination.tumor_size_y'
        db.add_column(u'exams_examination', 'tumor_size_y',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Examination.tumor_size_z'
        db.add_column(u'exams_examination', 'tumor_size_z',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Examination.tumor_volume'
        db.add_column(u'exams_examination', 'tumor_volume',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Examination.virsung_size'
        db.add_column(u'exams_examination', 'virsung_size',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Examination.distal_atrophy'
        db.add_column(u'exams_examination', 'distal_atrophy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Examination.lypomatosis'
        db.add_column(u'exams_examination', 'lypomatosis',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Examination.choledoch_diametr'
        db.add_column(u'exams_examination', 'choledoch_diametr',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Examination.bile_ducts_extension'
        db.add_column(u'exams_examination', 'bile_ducts_extension',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Examination.metastasis'
        db.add_column(u'exams_examination', 'metastasis',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Examination.lymphadenopathy'
        db.add_column(u'exams_examination', 'lymphadenopathy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Examination.ascit'
        db.add_column(u'exams_examination', 'ascit',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Examination.arterial_invasion'
        db.add_column(u'exams_examination', 'arterial_invasion',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Examination.portal_invasion'
        db.add_column(u'exams_examination', 'portal_invasion',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Phase.CT'
        db.add_column(u'exams_phase', 'CT',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['exams.CT']),
                      keep_default=False)

        # Deleting field 'Phase.examination'
        db.delete_column(u'exams_phase', 'examination_id')

        # Adding field 'Examination.act'
        db.add_column(u'exams_examination', 'act',
                      self.gf('django.db.models.fields.CharField')(max_length=4000, null=True),
                      keep_default=False)

        # Adding field 'Examination.conclusion'
        db.add_column(u'exams_examination', 'conclusion',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True),
                      keep_default=False)

        # Deleting field 'Examination.artefacts'
        db.delete_column(u'exams_examination', 'artefacts')

        # Deleting field 'Examination.tumor_size_x'
        db.delete_column(u'exams_examination', 'tumor_size_x')

        # Deleting field 'Examination.tumor_size_y'
        db.delete_column(u'exams_examination', 'tumor_size_y')

        # Deleting field 'Examination.tumor_size_z'
        db.delete_column(u'exams_examination', 'tumor_size_z')

        # Deleting field 'Examination.tumor_volume'
        db.delete_column(u'exams_examination', 'tumor_volume')

        # Deleting field 'Examination.virsung_size'
        db.delete_column(u'exams_examination', 'virsung_size')

        # Deleting field 'Examination.distal_atrophy'
        db.delete_column(u'exams_examination', 'distal_atrophy')

        # Deleting field 'Examination.lypomatosis'
        db.delete_column(u'exams_examination', 'lypomatosis')

        # Deleting field 'Examination.choledoch_diametr'
        db.delete_column(u'exams_examination', 'choledoch_diametr')

        # Deleting field 'Examination.bile_ducts_extension'
        db.delete_column(u'exams_examination', 'bile_ducts_extension')

        # Deleting field 'Examination.metastasis'
        db.delete_column(u'exams_examination', 'metastasis')

        # Deleting field 'Examination.lymphadenopathy'
        db.delete_column(u'exams_examination', 'lymphadenopathy')

        # Deleting field 'Examination.ascit'
        db.delete_column(u'exams_examination', 'ascit')

        # Deleting field 'Examination.arterial_invasion'
        db.delete_column(u'exams_examination', 'arterial_invasion')

        # Deleting field 'Examination.portal_invasion'
        db.delete_column(u'exams_examination', 'portal_invasion')


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
        u'exams.ct': {
            'Meta': {'object_name': 'CT'},
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
            'choledoch_diametr': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'distal_atrophy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lymphadenopathy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lypomatosis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'metastasis': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exams.Patient']"}),
            'portal_invasion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tumor_size_x': ('django.db.models.fields.IntegerField', [], {}),
            'tumor_size_y': ('django.db.models.fields.IntegerField', [], {}),
            'tumor_size_z': ('django.db.models.fields.IntegerField', [], {}),
            'tumor_volume': ('django.db.models.fields.IntegerField', [], {}),
            'virsung_size': ('django.db.models.fields.IntegerField', [], {})
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
            'tumor_size_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tumor_size_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tumor_size_z': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tumor_volume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'field': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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