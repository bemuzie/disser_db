from django import forms
from django.forms.extras import widgets
from exams.models import *
from exams import widgets as mywidgets

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        birth_date = forms.DateField(widget= widgets.SelectDateWidget())

        #fields =('fio','weight','birth_date')
class PatientForm_lite(forms.ModelForm):
	clinical_data = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Patient

		fields = ('clinical_data','weight')


class DocsForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields =('date','name','group','description','img')
        #widget = {'img':mywidgets.MultiFileInput}
