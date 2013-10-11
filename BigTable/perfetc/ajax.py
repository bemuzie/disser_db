# -*- coding: utf-8 -*-
from django.utils import simplejson 
from dajaxice.core import dajaxice_functions 
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from perfetc.models import *


@dajaxice_register
def show_graph(request,body_model_id):
	dajax = Dajax()
	
	body=Body.objects.get(examination=int(body_model_id))
	body_model=body.compartment_set.all()
	print 'body_model'
	print body_model
	nodes=''.join(["g.addNode('%s');"%i.name for i in body_model])
	edges=''.join(["g.addEdge('%s','%s',{ directed : true,label:'%s' });"%(i.from_compartment.name,i.to_compartment.name,i.weight) for i in Edge.objects.all()])
	dajax.script("""
	var redraw, g, renderer;
    var width = 400;
    var height = 400;
    
    g = new Graph();
    %s
    st = { directed: true, label : "Label",
            "label-style" : {
                "font-size": 20
            }
        };
    %s
    var layouter = new Graph.Layout.Spring(g);
    renderer = new Graph.Renderer.Raphael('canvas', g, width, height);

		"""%(nodes,edges))

	#dajax.alert(field)
	return dajax.json()
	
	
