from django.db import models

# Create your models here.
class Patient(models.Model):
	fio = models.CharField(max_length = 100)
	#birth_date = models.DateTimeField(default =0)
	weight = models.IntegerField(default =0)
	docs = models.CharField(max_length = 100)
	clinical_data = models.CharField(max_length = 500)
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
	ce_conc = models.IntegerField()
	ce_volume = models.IntegerField()
	ce_speed_suggested = models.IntegerField()
	ce_speed_real = models.IntegerField()
	ce_water_volume = models.IntegerField()
	ce_water_speed = models.IntegerField()

	date = models.DateTimeField()
	#exam_params = models.ForeighnKey(ExamParams)
	#patient = models.ForeighnKey(Patient)
	
	conclusion =  models.CharField(max_length = 500)

