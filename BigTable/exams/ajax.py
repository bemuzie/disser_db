# -*- coding: utf-8 -*-
from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from exams.models import *

from exams.forms import *


# @dajaxice_register
def primer(request, message):
    return_message = u'Полученное сообщение: {0}'.format(message)
    return simplejson.dumps({'message': return_message})


@dajaxice_register
def print_field(request, message, patient_id):
    dajax = Dajax()

    patient = Patient.objects.get(pk=int(patient_id))
    form = PatientForm_lite(deserialize_form(message),
                            instance=patient)

    if form.is_valid():
        dajax.remove_css_class('#patient div', 'has-error')
        form.save()
        print patient.clinical_data.lower()
        for tag in TagDictionary.objects.all():
            print tag.word, tag.tag
            if tag.word in patient.clinical_data.lower():
                print 1, tag.word, tag.tag
                patient.tags.add(tag.tag)
        dajax.script("""$('#patient_tags').html('<p> %s</p>')
					""" % (', '.join(patient.tags.names())))

    else:
        dajax.remove_css_class('#patient div', 'has-error')
        for er_field, er_text in form.errors.items():
            dajax.script("""$('#id_%s').parent().parent().addClass('has-error');"""
                         % er_field)





    #dajax.alert(field)
    return dajax.json()
	
	
