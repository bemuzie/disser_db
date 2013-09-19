# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from datetime import datetime
from taggit.managers import TaggableManager
from taggit.models import Tag, TaggedItem

# Create your models here.

class CyrillicTag (Tag):
	class Meta:
		proxy = True
	def slugify(self, tag, i=None):
		slug = tag.lower().replace(' ','-')
		if i is not None:
			slug += '-%d' % i
		return slug
class CyrillicTagedItem(TaggedItem):
	class Meta:
		proxy=True
	@classmethod
	def tag_model(cls):
		return CyrillicTag


class Patient(models.Model):
	fio = models.CharField(max_length = 100)
	birth_date = models.DateField(blank=True, null=True)
	weight = models.IntegerField(default =0)
	clinical_data = models.CharField(max_length = 500)
	tags = TaggableManager(through=CyrillicTagedItem,blank=True)
	def __unicode__(self):
		return self.fio

class Docs(models.Model):
	patient = models.ForeignKey(Patient,default=0)
	date = models.DateField(blank=True,null=True)
	img = models.FileField(upload_to = 'files')
	tags = TaggableManager(through=CyrillicTagedItem,blank=True)
	def __unicode__(self):
		return unicode(self.img)


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
							('M','MRI')),
				'contrast':(('O',u'Омнипак'),
							('U',u'Ультравист'),
							('Op',u'Оптирэй'),
							('V',u'Визипак')),
				'contrast_conc':((300,300),
								(320,320),
								(350,350),
								(380,380))}

	modality = models.CharField(max_length=1,choices = CHOICES['modalities'])
	ce_agent = models.CharField(max_length=10,choices = CHOICES['contrast'])
	ce_conc = models.IntegerField(default =0,choices = CHOICES['contrast_conc'])
	ce_volume = models.IntegerField(default =0)
	ce_speed_suggested = models.IntegerField(default =0)
	ce_speed_real = models.IntegerField(default =0)
	ce_water_volume = models.IntegerField(default =0)
	ce_water_speed = models.IntegerField(default =0)
	date = models.DateField(blank=True, null=True)
	conclusion =  models.CharField(max_length = 1000)
	patient=models.ForeignKey(Patient,default =0)
	tags = TaggableManager(through=CyrillicTagedItem,blank=True)

class Reminder(models.Model):
	CHOICES = {'done':((True,u'Сделано'),
						(False,u'Сделать'))}
	note = models.CharField(max_length = 140)
	remind_date = models.DateField(blank=True, null=True)
	done = models.BooleanField(default=False, choices = CHOICES['done'])
	patient = models.ForeignKey(Patient,default = 0)

class TagDictionary(models.Model):
	word = models.CharField(max_length=250)
	tag = models.ForeignKey(Tag, default = 0)



