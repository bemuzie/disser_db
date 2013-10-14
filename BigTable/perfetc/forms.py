from django import forms
from django.forms.extras import widgets
from peretc.models import *
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

class CompartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Compartment
        