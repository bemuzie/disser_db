# Create your views here.
from django.conf import settings
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.template import RequestContext, loader, Context
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.utils.encoding import smart_str
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.core.servers.basehttp import FileWrapper

from datetime import date
from exams.models import *
from perfetc.models import *
from perfetc.forms import *


@csrf_protect
def circulation(request, patient_id, examination_id):
    bodymodel = get_object_or_404(Body, examination=examination_id)
    compartmentForm = CompartmentForm

    return render(request, 'perfetc/graph.html', {'bodymodel': bodymodel,
                                                  'compartment_form': compartmentForm})