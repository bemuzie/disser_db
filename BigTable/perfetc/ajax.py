# -*- coding: utf-8 -*-
from django.utils import simplejson 
from dajaxice.core import dajaxice_functions 
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from perfetc.models import *
from perfetc.forms import *


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
	print compartment
