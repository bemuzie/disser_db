
# -*- coding: utf-8 -*-
import re
import os
import sys
import codecs
#import win32console 
from datetime import datetime

#PROJECT_ROOT = os.path.join('D:/GitHub/disser_db/BigTable/BigTable')
#sys.path.insert(0,PROJECT_ROOT)
from django.core.management import setup_environ
import BigTable.settings
setup_environ(BigTable.settings)
from exams.models import Patient,Examination,Perfusion
from django.core.exceptions import ObjectDoesNotExist

#os.popen('chcp').read()
#import locale
#encoding = locale.getpreferredencoding(do_setlocale=True)


"""
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
print sys.stdout.encoding # win32
win32console.SetConsoleCP(65001)
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
"""
#print sys.getdefaultencoding()
#print sys.stdout.encoding # win32

OUTPUT_DIR = '/home/denest/diss/R/data/'
output_csv= 'summary.csv'
f=open(os.path.join(OUTPUT_DIR,output_csv),'w')


table_dict={'patient': lambda exam:exam.patient.id,
			'age':lambda exam:(exam.date-exam.patient.birth_date).days/365,
			'gender': lambda exam:exam.patient.gender,
			'diagnosis': lambda exam:exam.patient.final_diagnosis,
			'date': lambda exam:exam.date,
			'chemo': lambda exam:exam.patient.procedure_set.filter(procedure='chemo',date__lt=exam.date) or 0,#how many courses of chemotherapy patient had before this examination
			'radio': lambda exam:exam.patient.procedure_set.filter(procedure='radio',date__lt=exam.date) or 0, #how many courses of radiotherapy patient had before this examination
			'exams': lambda exam:len(exam.patient.examination_set.filter(date__lt=exam.date)), #how many examinations patient had before this examination
			'arterial_inv_any': lambda exam: int(any(exam.__dict__[i]==4 for i in ['arterial_invasion_celiac',
																			   'arterial_invasion_messup',
																			   'arterial_invasion_splen',
																			   'arterial_invasion_hep',
																			   'arterial_invasion_other'])),
			'metastasis':lambda exam: exam.metastasis,
			'SCT_diagnosis': lambda exam:exam.patient.examination_set.filter(modality='CT') or 0,
			'MRI_diagnosis': lambda exam:exam.patient.examination_set.filter(modality='MR') or 0,
			'PET_diagnosis': lambda exam:exam.patient.examination_set.filter(modality='PT') or 0,
			
			}


first_line=table_dict.keys()
f.write(','.join(first_line)+'\n')
for ex in Examination.objects.all():
	try:
		f.write(','.join( [ str(table_dict[i](ex)) for i in first_line] )+'\n')
	except ValueError,s:
		print s
	except ObjectDoesNotExist,s:
		print s
		
f.close()