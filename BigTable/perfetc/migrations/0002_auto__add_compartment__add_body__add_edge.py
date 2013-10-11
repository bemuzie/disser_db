# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compartment'
        db.create_table(u'perfetc_compartment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfetc.Body'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('pdf', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('mean', self.gf('django.db.models.fields.FloatField')()),
            ('sigma', self.gf('django.db.models.fields.FloatField')()),
            ('parametr3', self.gf('django.db.models.fields.FloatField')()),
            ('injection', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'perfetc', ['Compartment'])

        # Adding model 'Body'
        db.create_table(u'perfetc_body', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('injection_duration', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'perfetc', ['Body'])

        # Adding model 'Edge'
        db.create_table(u'perfetc_edge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_compartment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_compartment', to=orm['perfetc.Compartment'])),
            ('to_compartment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_compartment', to=orm['perfetc.Compartment'])),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'perfetc', ['Edge'])


    def backwards(self, orm):
        # Deleting model 'Compartment'
        db.delete_table(u'perfetc_compartment')

        # Deleting model 'Body'
        db.delete_table(u'perfetc_body')

        # Deleting model 'Edge'
        db.delete_table(u'perfetc_edge')


    models = {
        u'perfetc.body': {
            'Meta': {'object_name': 'Body'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injection_duration': ('django.db.models.fields.IntegerField', [], {})
        },
        u'perfetc.compartment': {
            'Meta': {'object_name': 'Compartment'},
            'body': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perfetc.Body']"}),
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