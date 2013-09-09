from django.db import models
from django.forms import ModelForm
from datetime import datetime
# Create your models here.
class Patient(models.Model):
	fio = models.CharField(max_length = 100)
	birth_date = models.DateField(blank=True, null=True)
	weight = models.IntegerField(default =0)
	clinical_data = models.CharField(max_length = 500)
	def __unicode__(self):
		return self.fio

class Docs(models.Model):
	patient = models.ForeignKey(Patient,default=0)
	date = models.DateField(blank=True,null=True)
	name = models.CharField(max_length = 20)
	group = models.CharField(max_length = 20)
	description = models.CharField(max_length = 300)
	img = models.FileField(upload_to = 'files')

class ExamParams(models.Model):
	modality = models.CharField(max_length = 100)
	dcm_dump = models.CharField(max_length = 100)

class PerfusionCT(models.Model):
	data = models.CharField(max_length = 100)
	af = models.IntegerField(default =0)
	bv = models.IntegerField(default =0)
	mtt =models.IntegerField(default =0)

class Examination(models.Model):
	CHOICES = {'modalities':(('C','CT'),
							('P','Perfusion CT'),
							('M','MRI'))}

	modality = models.CharField(max_length=1,choices = CHOICES['modalities'])

	ce_agent = models.CharField(max_length=10)
	ce_conc = models.IntegerField(default =0)
	ce_volume = models.IntegerField(default =0)
	ce_speed_suggested = models.IntegerField(default =0)
	ce_speed_real = models.IntegerField(default =0)
	ce_water_volume = models.IntegerField(default =0)
	ce_water_speed = models.IntegerField(default =0)
	date = models.DateField(blank=True, null=True)
	conclusion =  models.CharField(max_length = 500)
	patient=models.ForeignKey(Patient,default =0)

