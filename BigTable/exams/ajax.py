# -*- coding: utf-8 -*-
from django.utils import simplejson 
from dajaxice.core import dajaxice_functions 
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax

@dajaxice_register
def primer(request,message):
    return_message=u'Полученное сообщение: {0}'.format(message)
    return simplejson.dumps({'message':return_message})

@dajaxice_register
def print_field(request,message):
	dajax = Dajax()

	
	#if field.is_valid():
	dajax.alert(deserialize_form(message))
	#dajax.alert(field)
	return dajax.json()
	
	
