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
	print 'body_model'
	print body_model
	nodes=''.join(["""var %(name)s = graph.newNode({label: '%(name)s',											
															});"""%{'name':i.name} 
															for i in body_model])
	edges=''.join(["graph.newEdge(%(from)s, %(to)s, {color: '#00A0B0',weight:%(weight)s,label:%(weight)s});"%
												{'from':i.from_compartment.name,
												'to':i.to_compartment.name,
												'weight':i.weight} 
												for i in Edge.objects.all()])
	dajax.script("""
	var graph = new Springy.Graph();
	%s
	%s
	jQuery(function(){
  var springy = window.springy = jQuery('#graph').springy({
    graph: graph,
    nodeSelected: function(node){
      console.log('Node selected: ' + JSON.stringify(node.data));
    }
  	});
	});
		"""%(nodes,edges))

	#dajax.alert(field)
	return dajax.json()
	
def show_concentration(request,body_model_id):
	new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'myfirstchart',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    { year: '2006', value: 20 },
    { year: '2009', value: 10 },
    { year: '2010', value: 5 },
    { year: '2011', value: 5 },
    { year: '2012', value: 20 }
  ],
  // The name of the data record attribute that contains x-values.
  xkey: 'year',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Value']
});

def get_compartment_form(request,body_model_id,compartment):
	dajax = Dajax()
	
	body=Body.objects.get(examination=int(body_model_id))
	body_model=body.compartment_set.all()
	compartment_form = CompartmentForm(instance=body.compartment_set.get(name=compartment))
	for i in compartment_form:
		
	return dajax.json()