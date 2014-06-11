
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

OUTPUT_DIR = '/home/denest/DISSER/R/data/'
output_csv= 'ts_summary.csv'
f=open(os.path.join(OUTPUT_DIR,output_csv),'w')


table_dict={'patient': lambda roi: roi.phase.examination.patient.id,
			'exam': lambda roi:roi.phase.examination.id,
			'roi' : lambda roi:roi.roi,
			't' : roi.phase.time,
			'median' : roi.density
			}


first_line=table_dict.keys()
f.write(','.join(first_line)+'\n')
for ex in Examination.objects.all():
	for t in ex.phase_set.all():
		for roi in t.density_set.all():

			try:
				f.write(','.join( [ str(table_dict[i](ex)) for i in first_line] )+'\n')
			except ValueError,s:
				print s
			except ObjectDoesNotExist,s:
				print s
		
f.close()