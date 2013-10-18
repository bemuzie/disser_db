from django import forms
from django.forms.extras import widgets
from perfetc.models import *
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

class CompartmentForm(forms.ModelForm):
    class Meta:
        model = Compartment
        fields = ('name','pdf','mean','sigma','parametr3','injection')

class EdgeForm(forms.ModelForm):
    class Meta:
        model = Edge
        
EdgeFormSet_output = modelformset_factory(Edge,extra=0,max_num=None,fields=('to_compartment', 'weight'))
EdgeFormSet_input = modelformset_factory(Edge,extra=0,max_num=None,fields=('from_compartment', 'weight'))