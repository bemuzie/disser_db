# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.utils.encoding import smart_str
from django.core.urlresolvers import reverse


from exams.models import *
from exams.forms import *


def index(request):
	template = loader.get_template('reports/index.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def patient_list(request):
	latest_patients_list = Patient.objects.order_by('-fio')
	exams_num_list = [len(i.examination_set.all()) for i in latest_patients_list]
	latest_patients_list = zip(latest_patients_list,exams_num_list)


	template = loader.get_template('reports/patient_list.html')
	context = RequestContext(request, {'latest_patients_list':latest_patients_list})
	return HttpResponse(template.render(context))

def detail(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	patient_form = PatientForm(request.POST or None,instance=patient)
	if patient_form.is_valid():
		patient_form.save()
		patient_form = PatientForm(instance=patient)
		
	examinations = patient.examination_set.all()
	template = loader.get_template('reports/detail.html')
	docs_form = DocsForm(request.POST or None,request.FILES or None)
	if docs_form.is_valid():
		docs_form.save(commit=False)
		docs_form.patient=patient
		
		patient.docs_set.add(docs_form.instance)
		docs_form = DocsForm()
		return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
	
	return render(request,'reports/detail.html',{'patient':patient,
												'examinations' : examinations, 
												'docs_form':docs_form,
												"patient_form":patient_form

												})

def add_patient(request):
	patient_form = PatientForm(request.POST or None)
	if patient_form.is_valid():
		patient_form.save()
		patient_form = PatientForm()
	return render (request,'reports/new_patient.html',
		{'form':patient_form,
		'all_is_right':all_is_right})



