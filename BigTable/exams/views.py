# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.utils.encoding import smart_str



from exams.models import *
from exams.forms import *



def index(request):
	latest_patients_list = Patient.objects.order_by('-fio')
	exams_num_list = [len(i.examination_set.all()) for i in latest_patients_list]
	latest_patients_list = zip(latest_patients_list,exams_num_list)


	template = loader.get_template('reports/index.html')
	context = RequestContext(request, {'latest_patients_list':latest_patients_list})
	return HttpResponse(template.render(context))

def detail(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	examinations = patient.examination_set.all()
	template = loader.get_template('reports/detail.html')
	docs_form = DocsForm(initial = {'patient':patient})
	print dir(docs_form)
	return render(request,'reports/detail.html',{'patient':patient,
												'examinations' : examinations, 
												'docs_form':docs_form
												})

def new_patient(request):
	all_is_right='	'
	if request.method == 'POST':
		form = PatientForm(request.POST)
		if form.is_valid():
			form.save()
			all_is_right = u'новый пациент зарегистрирован'
			form = PatientForm()
	else:
		form = PatientForm()
	return render (request,'reports/new_patient.html',
		{'form':form,
		'all_is_right':all_is_right})
def add_doc(request, patient_id):
	print 1
	p = get_object_or_404(Patient, pk=patient_id)
	if request.method == 'POST':
		docs_form = DocsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			docs_form = DocsForm()
	else:
		docs_form = DocsForm()
	return 	HttpResponseRedirect(reverse('exams.views.detail', args=(p.id,)))


