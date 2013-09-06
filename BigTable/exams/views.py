# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from exams.models import Patient,Examination

def index(request):
	latest_patients_list = Patient.objects.order_by('-fio')
	template = loader.get_template('reports/index.html')
	context = RequestContext(request, {'latest_patients_list':latest_patients_list})
	return HttpResponse(template.render(context))

def detail(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	
	examinations = list(Examination.objects.filter(patient=patient_id))
	if not examinations:
		examinations = 1
	template = loader.get_template('reports/detail.html')
	return render(request,'reports/detail.html',{'patient':patient,'examinations' : examinations})