# -*- coding: utf-8 -*-
from django.utils import simplejson 
from dajaxice.core import dajaxice_functions 
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from perfetc.models import *
from perfetc.forms import *
from django.core.context_processors import csrf

import numpy as np
import circulation_models

global_body_model={}


@dajaxice_register
def show_graph(request,body_model_id):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	body_model=body.compartment_set.all()
	nodes = [i.name for i in body_model]
	edges=[]
	for node in body_model:
		edges.extend([[i.from_compartment.name, i.to_compartment.name,{'label':i.weight}] 
									for i in Edge.objects.filter(from_compartment=node)])

	graphJSON = {"nodes":nodes, "edges":edges}
	print graphJSON
	dajax.add_data(graphJSON,'graph.loadJSON')
	
	return dajax.json()

@dajaxice_register
def node_props(request,body_model_id,nodename):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	compartment=body.compartment_set.get(name=nodename)
	
	form = CompartmentForm(instance=compartment)
		

	dajax.assign('#compartment', 'innerHTML',form.as_p())
	return dajax.json()

@dajaxice_register
def change_model(request,compartment_form,body_model_id):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	form=CompartmentForm(deserialize_form(compartment_form))
	compartment=body.compartment_set.get(name=form['name'].value())
	form.instance=compartment
	
	if form.is_valid():
		print 'ok'
		form.save()
		

	else:
		for er_field,er_text in form.errors.items():
			dajax.script("""$('#id_%s').parent().parent().addClass('has-error');"""
				%er_field)
	JSONdata=make_circul_model(int(body_model_id),200,1,['concentration','transit_times'])

	#print JSONdata
	dajax.add_data(JSONdata,'draw_concentration_plot')
	
	return dajax.json()

def plot_concentration(request,body_model_id,time_duration,time_resolution):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	nodes = [i.name for i in body_model]
	body_dict = {"nodes":[i.name for i in body_model],
					"edges":[[i.from_compartment.name, i.to_compartment.name,{'label':i.weight}]
					 for i in Edge.objects.all()]}


	return dajax.json()
@dajaxice_register
def make_circul_model(body_model_id,time_duration,time_resolution,return_data='concentration'):
	dajax = Dajax()
	body=Body.objects.get(examination=int(body_model_id))
	body_model=body.compartment_set.all()
	circul_model={}

	for node in body.compartment_set.all():
		tmp_node=circulation_models.Compartment_fft(node.name)
		tmp_node.set_time(time_duration,time_resolution)
		tmp_node.set_attrs (node.mean, node.sigma, node.parametr3)
		if node.injection:
			tmp_node.make_delta()
		else:
			tmp_node.make_profile()
		circul_model[node.name] = tmp_node
	for node in body.compartment_set.all():
		[circul_model[node.name].add_successor(circul_model[edge.to_compartment.name],edge.weight) 
									for edge in Edge.objects.filter(from_compartment=node)]
	
	circul_model[ body.compartment_set.get(injection=True).successors.all()[0].name]()
	JSONdata=[]
	if 'concentration' in return_data:
		JSONdata.append([{'label':n,'data':map(list,zip(c.time.tolist(),c.concentration.tolist()))} for n,c in circul_model.items()])
	#JSONdata = [[[1,2],[4,3],[5,3]]]
	if 'transit_times' in return_data:
		JSONdata.append([{'label':n,'data':map(list,zip(c.time.tolist(),c.profile.tolist()))} for n,c in circul_model.items()])
	
	
	return JSONdata
