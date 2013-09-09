
# -*- coding: utf-8 -*-
import re
import os
import sys
import codecs
#import win32console 
from datetime import datetime

PROJECT_ROOT = os.path.join('D:/GitHub/disser_db/BigTable/BigTable')
#sys.path.insert(0,PROJECT_ROOT)
from django.core.management import setup_environ
import BigTable.settings
setup_environ(BigTable.settings)
from exams.models import Patient,Examination


os.popen('chcp').read()
import locale
encoding = locale.getpreferredencoding(do_setlocale=True)


"""
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
print sys.stdout.encoding # win32
win32console.SetConsoleCP(65001)
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
"""
print sys.getdefaultencoding()
print sys.stdout.encoding # win32

p='acts'

def low(string):
	return unicode(string,'utf-8').lower().encode('utf-8')
def list_in_str(l,s):
	return any([i in s for i in l])

def time_extract(time_str):
	date_str ='-'.join([j for j in re.split('\D',time_str) if j])
	try:
		d=datetime.strptime(date_str, '%d-%m-%Y')
	except ValueError:
		try: 
			d=datetime.strptime(date_str, '%d-%m-%y')
		except ValueError:
			try:
				d=datetime.strptime(date_str, '%Y')
			except ValueError:
				return None
	return d

out_file = file('table','w')


for root, dirs, files in os.walk(os.path.join(p)):
	for i in files:
		print i
		f=open(os.path.join(p,i))
		f_list = f.readlines()
		for l in f_list:
			if 'ФИО' in l:
				fio=l.replace(' ','').replace("ФИО:",'').replace('\n','').replace('\r','')
			elif 'Год рождения' in l:
				gr = time_extract(l)
			elif 'Дата исследования:' in l:
				dr = time_extract(l)
				print dr
			elif 'Клинические данные' in l:

				kd= l.replace("Клинические данные:",'').replace('\n','')
			elif 'Заключение' in l:
				z_fr=f_list.index(l)
				try:
					z_to=[i for i,j in enumerate(f_list) if 'Нестеров' in j][0]
				except:
					x_to=-1
				
				z= ' '.join( f_list[ z_fr : z_to] ).replace("Заключение:",'').replace('\n','')

		kd2 = low(kd).replace(' ','').replace('-','')
		z2 = low(z).replace(' ','').replace('-','')
		deseases = {"по": "",
					"РПЖ": "",
					"НРПЖ": "",
					"панкреатит": "",
					"???": "",}

		if list_in_str(["пдр","резекциихв","резекциипод"],kd2) :
			group_desease = 'по'
		elif list_in_str(['нейроэнд'],kd2):
			group_desease = 'НРПЖ'
		elif 'опухоль' in z2:
			group_desease = 'РПЖ'
		elif "панкреатит" in low(kd) or "панкреатит" in low(z):
			group_desease = 'панкреатит'
		else:
			group_desease = '???'

		po_d={'стентирование':['стент'],
			'дренирование':['дренир'],
			'химиотерапия':['хим','рхт'],
			'лучевая терапия':['луч'],
			'наложение анастамоза':['анаст']
			}
		po = ', '.join([i for i,j in po_d.items() if list_in_str(j,low(kd))])


		if all([fio,gr,kd,z,dr]) and 'подж' in kd or 'подж' in z : 

			patient = Patient.objects.get_or_create(fio = fio, birth_date=gr)[0]
			
			patient.clinical_data +=unicode(kd,'utf-8')
			patient.save()
			examination = Examination(conclusion=z,date=dr)
			patient.examination_set.add(examination)
			
			
			#out_file.write('%s|%s|%s|%s|%s|%s|%s\n'%(fio,gr,dr,kd,z,group_desease,po))


