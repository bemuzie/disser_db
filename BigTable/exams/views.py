# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
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
	print request.GET


	return HttpResponse(template.render(context))

def patient_list(request):
	search_field = request.GET.get('search') or ''
	latest_patients_list = Patient.objects.filter(fio__regex=r'(%s|%s)'%(search_field,search_field.capitalize())).order_by('-fio')
	exams_num_list = [len(i.examination_set.all()) for i in latest_patients_list]
	latest_patients_list = zip(latest_patients_list,exams_num_list)
	template = loader.get_template('reports/patient_list.html')
	context = RequestContext(request, {'latest_patients_list':latest_patients_list})
	return HttpResponse(template.render(context))

def detail(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	patient_form = PatientForm_lite(instance=patient)
	examinations = patient.examination_set.all()
	docs_form = DocsForm()
	ReminderFormSet = formset_factory(ReminderForm,extra=0,max_num=1)
	reminder_formset = ReminderFormSet(initial = [{'patient':patient_id}])
	print reminder_formset[0].instance.done
	if request.POST.get('patient_submit'):
		print "Patient"
		patient_form = PatientForm_lite(request.POST or None,instance=patient)
		if patient_form.is_valid():
			patient_form.save()
			patient_form = PatientForm_lite(instance=patient)
	elif request.POST.get('docs_submit'):
		print "Docs"
		docs_form = DocsForm(request.POST or None,request.FILES or None)
		if docs_form.is_valid():
			docs_form.save(commit=False)
			docs_form.patient=patient
			
			patient.docs_set.add(docs_form.instance)
			docs_form = DocsForm()
			return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
	elif request.POST.get('change'):
		print "change",request.POST
		new_examination(request, patient_id)
	elif request.POST.get('delete'):
		print "delete"


	
	return render(request,'reports/detail.html',{'patient':patient,
												'examinations' : examinations, 
												'docs_form':docs_form,
												"patient_form":patient_form,
												'reminder_formset':reminder_formset

												})

def add_patient(request):
	patient_form = PatientForm(request.POST or None)
	if patient_form.is_valid():
		patient_form.save()

		return HttpResponseRedirect(reverse('exams.views.detail', args=(patient_form.instance.id,)))
	return render (request,'reports/add_patient.html',
		{'form':patient_form,})
def new_examination(request, patient_id, examination_id=None):
	patient = get_object_or_404(Patient, pk=patient_id)
	if examination_id:
		examination_form = ExaminationForm(request.POST or None, 
										instance = patient.examination_set.get(pk=examination_id))
	else:
		examination_form = ExaminationForm(request.POST or None)
		
	if examination_form.is_valid():
		examination_form.save(commit=False)
		examination_form.patient=patient
		patient.examination_set.add(examination_form.instance)
		return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
	return render(request, 'reports/add_examination.html', {'patient':patient,
															'examination_form':examination_form})

def modify_examination(request, patient_id, examination_id):
	
	if request.POST.get('delete'):
		patient = get_object_or_404(Patient, pk=patient_id)
		patient.examination_set.get(pk=examination_id).delete()
		return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
	elif request.POST.get('modify'):
		return HttpResponseRedirect(reverse('exams.views.new_examination', args=(patient_id,examination_id)))
	else:
		raise Http404

def modify_reminder(request, patient_id):
	
	patient = get_object_or_404(Patient, pk=patient_id)
	last_reminder_form = ReminderForm(request.POST)
	print last_reminder_form
	print request.POST
	if request.POST.get("new_reminder"):
		if last_reminder_form.is_valid():
			print valid
			patient.reminder_set.add(last_reminder_form.instance)
	if request.POST.get("change_reminder"):
		
		return HttpResponse(status=204)


