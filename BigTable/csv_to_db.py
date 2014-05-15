
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
#import BigTable.settings
#setup_environ(BigTable.settings)
from exams.models import Patient,Examination


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
EXAM_NUMBER = 0

f=open(os.path.join(ROOT,FILE))
f_list = f.readlines()
f_list = [i.split(',') for i in f_list]


for roi in f_list[1:]:
	
	perfusion_parametrs = dict([[par_name, par_value] for par_name, par_value in zip(f_list[0],roi):])
	perf_pars = Perfusion.get_or_create(roi=perfusion_parametrs['ROI'],examination=EXAM_NUMBER)
	examination.perfusion_set.add(perf_pars)
	examination.save()
