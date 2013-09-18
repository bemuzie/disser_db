# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TagDictionary'
        db.create_table(u'exams_tagdictionary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['taggit.Tag'])),
        ))
        db.send_create_signal(u'exams', ['TagDictionary'])

        # Deleting field 'Docs.group'
        db.delete_column(u'exams_docs', 'group')

        # Deleting field 'Docs.description'
        db.delete_column(u'exams_docs', 'description')

        # Deleting field 'Docs.name'
        db.delete_column(u'exams_docs', 'name')


        # Changing field 'Reminder.done'
        db.alter_column(u'exams_reminder', 'done', self.gf('django.db.models.fields.BooleanField')())

    def backwards(self, orm):
        # Deleting model 'TagDictionary'
        db.delete_table(u'exams_tagdictionary')


        # User chose to not deal with backwards NULL issues for 'Docs.group'
        raise RuntimeError("Cannot reverse this migration. 'Docs.group' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Docs.group'
        db.add_column(u'exams_docs', 'group',
                      self.gf('django.db.models.fields.CharField')(max_length=20),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Docs.description'
        raise RuntimeError("Cannot reverse this migration. 'Docs.description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Docs.description'
        db.add_column(u'exams_docs', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=300),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Docs.name'
        raise RuntimeError("Cannot reverse this migration. 'Docs.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Docs.name'
        db.add_column(u'exams_docs', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=20),
                      keep_default=False)


        # Changing field 'Reminder.done'
        db.alter_column(u'exams_reminder', 'done', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'ce_agent': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ce_conc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_speed_real': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_speed_suggested': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_volume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_water_speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ce_water_volume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'conclusion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'clinical_data': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
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