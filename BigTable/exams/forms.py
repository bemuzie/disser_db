from django import forms
from django.forms.extras import widgets
from exams.models import *
from exams import widgets as mywidgets
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['id'] = 'dp2'
        self.fields['birth_date'].widget.attrs['data-date-format'] = "dd.mm.yyyy"
        self.fields['birth_date'].widget.attrs['value'] = "02/16/2013"
        
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
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control '
         
    def inline(self):
        return self._html_output(
            normal_row = u'<div class="form-group" >%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row = u'<div class="form-group has-error has-warning">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)
    class Meta:
        model = Docs
        fields =('date','img')
        #widget = {'img':mywidgets.MultiFileInput}


class ExaminationForm(forms.ModelForm):
    
    conclusion = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = Examination
        exclude = 'patient'

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        
ReminderFormSet = modelformset_factory(Reminder,extra=1,max_num=None,fields=('note', 'remind_date'))

class PhaseForm(forms.ModelForm):
    class Meta:
        model = Phase

PhaseFormSet = modelformset_factory(Phase,extra=1,max_num=None,fields=('time', 'zone'))
