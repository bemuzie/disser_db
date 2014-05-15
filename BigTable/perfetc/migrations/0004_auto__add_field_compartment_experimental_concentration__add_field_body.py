# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Compartment.experimental_concentration'
        db.add_column(u'perfetc_compartment', 'experimental_concentration',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Body.experimental_time_axis'
        db.add_column(u'perfetc_body', 'experimental_time_axis',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Compartment.experimental_concentration'
        db.delete_column(u'perfetc_compartment', 'experimental_concentration')

        # Deleting field 'Body.experimental_time_axis'
        db.delete_column(u'perfetc_body', 'experimental_time_axis')


    models = {
        u'perfetc.body': {
            'Meta': {'object_name': 'Body'},
            'examination': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'experimental_time_axis': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injection_duration': ('django.db.models.fields.IntegerField', [], {})
        },
        u'perfetc.compartment': {
            'Meta': {'object_name': 'Compartment'},
            'body': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfetc.Body']"}),
            'experimental_concentration': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mean': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'parametr3': ('django.db.models.fields.FloatField', [], {}),
            'pdf': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sigma': ('django.db.models.fields.FloatField', [], {}),
            'successors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['perfetc.Compartment']", 'through': u"orm['perfetc.Edge']", 'symmetrical': 'False'})
        },
        u'perfetc.edge': {
            'Meta': {'object_name': 'Edge'},
            'from_compartment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_compartment'", 'to': u"orm['perfetc.Compartment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_compartment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_compartment'", 'to': u"orm['perfetc.Compartment']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['perfetc']