# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from datetime import datetime
from taggit.managers import TaggableManager
from taggit.models import Tag, TaggedItem

# Create your models here.

class CyrillicTag(Tag):
    class Meta:
        proxy = True

    def slugify(self, tag, i=None):
        print type(tag)
        print tag, i
        slug = tag.lower().replace(' ', '-')
        if i is not None:
            slug += '-%d' % i
        return slug


class CyrillicTagedItem(TaggedItem):
    class Meta:
        proxy = True

    @classmethod
    def tag_model(cls):
        return CyrillicTag


# ##Patient information
class Patient(models.Model):
    CHOICES = {'gender': (('m', 'male'),
                          ('f', 'female'))}

    fio = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=CHOICES['gender'])
    weight = models.IntegerField(blank=True, null=True)
    clinical_data = models.CharField(max_length=500)
    tags = TaggableManager(through=CyrillicTagedItem, blank=True)
    final_diagnosis = models.CharField(max_length=100)

    ###Anamnes

    def __unicode__(self):
        return self.fio


class Procedure(models.Model):
    """Information about treatment and other procedures"""
    procedure = models.CharField(max_length=40)
    date = models.DateField(blank=True)
    text = models.CharField(max_length=100, blank=True)
    patient = models.ForeignKey(Patient, default=0)


class Analysis(models.Model):
    name = models.CharField(max_length=40)
    value = models.FloatField()
    date = models.DateField(blank=True, null=True, )
    patient = models.ForeignKey(Patient, default=0)


class ClinicalData(models.Model):
    date = models.DateField(blank=True, null=True)
    text = models.CharField(max_length=500)
    value = models.IntegerField(blank=True, null=True)
    patient = models.ForeignKey(Patient, default=0)


class Docs(models.Model):
    patient = models.ForeignKey(Patient, default=0)
    date = models.DateField(blank=True, null=True)
    img = models.FileField(upload_to='files')
    tags = TaggableManager(through=CyrillicTagedItem, blank=True)

    def __unicode__(self):
        return unicode(self.img)


class PerfusionCT(models.Model):
    data = models.CharField(max_length=100)
    af = models.IntegerField(default=0)
    bv = models.IntegerField(default=0)
    mtt = models.IntegerField(default=0)


class Examination(models.Model):
    CHOICES = {'modalities': (('CT', 'CT'),
                              ('PCT', 'Perfusion CT'),
                              ('MRI', 'MRI'),
                              ('PET', 'PET'),
                              ('EUS', 'EUS')),

               'contrast': (('O', u'Омнипак'),
                            ('U', u'Ультравист'),
                            ('Op', u'Оптирэй'),
                            ('V', u'Визипак')),
               'contrast_conc': ((300, 300),
                                 (320, 320),
                                 (350, 350),
                                 (370, 370)),

               'metastasis': ((0, u'Нет'),
                              (1, u'Есть'),
                              (2, u'Неопределенно'),
               ),
               'arterial_invasion': ((0, u'Нет'),
                                     (1, u'<50%'),
                                     (2, u'50-75%'),
                                     (3, u'>75%'),
                                     (4, u'Есть')
               ),
               'portal_invasion': ((0, u'Нет'),
                                   (1, u'Возможно'),
                                   (2, u'Есть')
               )}

    modality = models.CharField(max_length=3, choices=CHOICES['modalities'])
    ce_agent = models.CharField(max_length=10, choices=CHOICES['contrast'])
    ce_conc = models.IntegerField(default=0, choices=CHOICES['contrast_conc'])
    ce_volume = models.IntegerField(default=0)
    ce_speed_suggested = models.IntegerField(default=0)
    ce_speed_real = models.IntegerField(default=0)
    ce_water_volume = models.IntegerField(default=0)
    ce_water_speed = models.IntegerField(default=0)
    date = models.DateField(blank=True, null=True)
    artefacts = models.CharField(max_length=1000, null=True)

    #Act
    ##		Tumor



    ##		Pancreas
    virsung_size = models.IntegerField(default=0)
    distal_atrophy = models.BooleanField()
    lypomatosis = models.BooleanField()


    ##		Liver
    choledoch_diametr = models.IntegerField(default=0)
    bile_ducts_extension = models.BooleanField()
    metastasis = models.IntegerField(default=0, choices=CHOICES['metastasis'])

    ##		Other
    lymphadenopathy = models.BooleanField()
    ascit = models.BooleanField()
    arterial_invasion_celiac = models.IntegerField(default=0, choices=CHOICES[
        'arterial_invasion'])  # 0 - exact no, 1 - <50%, 2 - 50-75%, 3 >75%, 4 - exact yes
    arterial_invasion_messup = models.IntegerField(default=0, choices=CHOICES[
        'arterial_invasion'])  # 0 - exact no, 1 - <50%, 2 - 50-75%, 3 >75%, 4 - exact yes
    arterial_invasion_splen = models.IntegerField(default=0, choices=CHOICES[
        'arterial_invasion'])  # 0 - exact no, 1 - <50%, 2 - 50-75%, 3 >75%, 4 - exact yes
    arterial_invasion_hep = models.IntegerField(default=0, choices=CHOICES[
        'arterial_invasion'])  # 0 - exact no, 1 - <50%, 2 - 50-75%, 3 >75%, 4 - exact yes
    arterial_invasion_other = models.IntegerField(default=0, choices=CHOICES[
        'arterial_invasion'])  # 0 - exact no, 1 - <50%, 2 - 50-75%, 3 >75%, 4 - exact yes
    portal_invasion = models.IntegerField(default=0, choices=CHOICES[
        'portal_invasion'])  # 0 - exact no, 1 - probable, 2 - exact yes

    ##PCT


    #links
    patient = models.ForeignKey(Patient, default=0)


### Показатели

class Phase(models.Model):
    time = models.IntegerField(default=0)
    zone = models.CharField(max_length=40)
    examination = models.ForeignKey(Examination, default=0)

    class Meta:
        ordering = ['time']


class Density(models.Model):
    """
	Class to store CT numbers of specific areas respectively to phase
	"""
    density = models.IntegerField()
    roi = models.CharField(max_length=10)
    phase = models.ForeignKey(Phase, default=0)


class Perfusion(models.Model):
    roi = models.CharField(max_length=10)
    roi_size_max = models.IntegerField(default=0)
    roi_max_distance = models.IntegerField(default=0)
    roi_volume = models.IntegerField(default=0)

    bf_mean = models.IntegerField(default=0)
    bf_sd = models.IntegerField(default=0)
    bf_median = models.IntegerField(default=0)
    bf_quantile_low = models.IntegerField(default=0)
    bf_quantile_up = models.IntegerField(default=0)

    bv_mean = models.IntegerField(default=0)
    bv_sd = models.IntegerField(default=0)
    bv_median = models.IntegerField(default=0)
    bv_quantile_low = models.IntegerField(default=0)
    bv_quantile_up = models.IntegerField(default=0)

    mtt_mean = models.IntegerField(default=0)
    mtt_sd = models.IntegerField(default=0)
    mtt_median = models.IntegerField(default=0)
    mtt_quantile_low = models.IntegerField(default=0)
    mtt_quantile_up = models.IntegerField(default=0)

    #ttp - time to peak
    ttp = models.IntegerField(default=0)
    examination = models.ForeignKey(Examination, default=0)


class Reminder(models.Model):
    CHOICES = {'done': ((True, u'Сделано'),
                        (False, u'Сделать'))}
    note = models.CharField(max_length=140)
    remind_date = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False, choices=CHOICES['done'])
    patient = models.ForeignKey(Patient, default=0)


class TagDictionary(models.Model):
    word = models.CharField(max_length=250)
    tag = models.ForeignKey(CyrillicTag, default=0)

    def __unicode__(self):
        return self.word


