
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

from django.core.exceptions import ObjectDoesNotExist
from exams.models import Patient,Examination,Perfusion,Density,Phase


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

ROOT = '/home/denest/EXAMPLE_PATIENT/Volumes/DCM/20120216_301'
FILE = 'time_info.txt'
EXAM_NUMBER = 66

f=open(os.path.join(ROOT,FILE))
f_list = f.readlines()
f_list = [i[:-1].split(',') for i in f_list]
f_dict = {0:[]}

for i in f_list:
	print i
	try:
		f_dict[i[1]]+=[i[0]]
	except:
		f_dict[i[1]]=[i[0]]

print f_list
examination = Examination.objects.get(pk=EXAM_NUMBER)

#phases = f_list[0][1:] #extract just phases

all_data=[{'time':1,'roi':'liver','density':21}]
for phase_time,volumes in f_dict.items():
	phase=examination.phase_set.get_or_create(time=phase_time,zone=','.join(volumes))	


		#print dens[0].density
	


