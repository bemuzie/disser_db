
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

ROOT = './'
FILE = 'example.csv'
EXAM_NUMBER = 9

f=open(os.path.join(ROOT,FILE))
f_list = f.readlines()
f_list = [i[:-1].split(';') for i in f_list]
print f_list
examination = Examination.objects.get(pk=EXAM_NUMBER)

for roi in f_list[1:]:
	print roi
	perfusion_parametrs = dict([[par_name, par_value] for par_name, par_value in zip(f_list[0],roi)])
	print perfusion_parametrs
	perf_pars = Perfusion.objects.get_or_create(roi=perfusion_parametrs['roi'],examination=EXAM_NUMBER)
	perf_pars = examination.perfusion_set.get_or_create(examination=EXAM_NUMBER,**perfusion_parametrs)
	Perfusion(perfusion_parametrs)
	print dir(perf_pars)
	
	examination.save()
