from django import forms
from django.forms.extras import widgets
from exams.models import *
from exams import widgets as mywidgets

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        birth_date = forms.DateField(widget= widgets.SelectDateWidget())

        #fields =('fio','weight','birth_date')

class DocsForm(forms.ModelForm):
    class Meta:
        model = Docs

        #widget = {'img':mywidgets.MultiFileInput}

