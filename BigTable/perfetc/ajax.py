# -*- coding: utf-8 -*-
from django.utils import simplejson 
from dajaxice.core import dajaxice_functions 
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from perfetc.models import *
from perfetc.forms import *
from django.core.context_processors import csrf

global_body_model={}


@dajaxice_register
def show_graph(request,body_model_id):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	body_model=body.compartment_set.all()
	graphJSON = {"nodes":[i.name for i in body_model],
					"edges":[[i.from_compartment.name, i.to_compartment.name,{'label':i.weight}]
					 for i in Edge.objects.all()]}
	dajax.add_data(graphJSON,'graph.loadJSON')
	
	return dajax.json()

@dajaxice_register
def node_props(request,body_model_id,nodename):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	compartment=body.compartment_set.get(name=nodename)
	print request
	form = CompartmentForm(instance=compartment)
	
	print form.as_p()

	

	dajax.assign('#compartment', 'innerHTML',form.as_p())
	return dajax.json()

@dajaxice_register
def change_model(request,compartment_form,body_model_id):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	form=CompartmentForm(deserialize_form(compartment_form))
	compartment=body.compartment_set.get(name=form['name'].value())
	print compartment
	form.instance=compartment
	
	if form.is_valid():
		print 'ok'
		form.save()
		global_body_model[compartment.name].set_attrs

	else:
		for er_field,er_text in form.errors.items():
			dajax.script("""$('#id_%s').parent().parent().addClass('has-error');"""
				%er_field)
def plot_concentration(request,body_model_id):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	 dajax.json()
def make_gen_model(body):
	gen_body={}
	for node in body.compartment_set.all():
		gen_body[node.name]=general_model.Compartment_fft(node.name)
		gen_body[node.name].set_attrs([node.pdf,node.mean,node.sigma,mode.parametr3])
	gen_body['Lungs']()
	return gen_body
