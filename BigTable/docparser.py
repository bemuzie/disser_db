
# -*- coding: utf-8 -*-
import os
import sys
import codecs
import win32console 

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

out_file = file('table','w')


for root, dirs, files in os.walk(os.path.join(p)):
	for i in files:
		print i.decode('cp1251').encode('utf-8')
		f=open(os.path.join(p,i))
		f_list = f.readlines()
		for l in f_list:
			if 'ФИО' in l:
				fio=l.replace(' ','').replace("ФИО:",'').replace('\n','')
			elif 'Год рождения' in l:
				gr = l.replace(' ','').replace("Годрождения:",'').replace('\n','')
			elif 'Дата исследования:' in l:
				dr = l.replace(' ','').replace("Датаисследования:",'').replace('\n','')
			elif 'Клинические данные' in l:
				kd= l.replace("Клинические данные:",'').replace('\n','')
			elif 'Заключение' in l:
				z_fr=f_list.index(l)
				try:
					z_to=[i for i,j in enumerate(f_list) if 'Нестеров' in j][0]
				except:
					x_to=-1
				print z_to
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


		if 'подж' in kd or 'подж' in z:
			patient = Patient(fio = fio, clinical_data = kd)
			print patient.id
			patient.save()
			print patient.id
			
			examination = Examination(conclusion=z,patient=patient)
			
			examination.save()
			
			out_file.write('%s|%s|%s|%s|%s|%s|%s\n'%(fio,gr,dr,kd,z,group_desease,po))


