from django import forms
from django.forms.extras import widgets
from perfetc.models import *
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

class CompartmentForm(forms.ModelForm):
    class Meta:
        model = Compartment
        