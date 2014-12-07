
import numpy as np
from random import randrange
from datetime import timedelta,datetime,time

out_file = open('/home/denest/diss/R/data/summary_test.csv','w')


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    
    random_second = randrange(delta.days)
    return (start + timedelta(days=random_second))
d1 = datetime.strptime('1/1/2012', '%m/%d/%Y')
d2 = datetime.strptime('4/4/2014', '%m/%d/%Y')
zerotime=datetime(1970, 1, 1)
def make_line():
	patient_id = np.random.randint(0,100)
	gender = np.random.randint(0,2) and 'm' or 'f'
	age = np.random.randint(41,86)
	diagnosis = np.random.binomial(2,0.6) # 0 - 
	chemo = np.random.randint(0,2)
	chemo_date = random_date(d1,d2)
	radio = np.random.randint(0,2)
	radio_date = random_date(d1,d2)
	conc_elevation = np.random.randint(0,1)

	exam_id = np.random.randint(0,200)
	exam_date = random_date(d1,d2)
	exam_date_abs = exam_date - zerotime



	


	atrophy = diagnosis==2 and np.random.binomial(1,0.3) or 0
	lipomatosis = np.random.binomial(1,0.2)


	ce_aorta_max_hu = np.random.normal(150,20)
	ce_aorta_max_t = np.random.randint(10,25)
	ce_pancreas_max_hu = ce_aorta_max_hu*(0.5+0.4*np.random.random())  - (atrophy==1 and np.random.randint(10,30)) - (lipomatosis==1 and np.random.randint(10,30))
	ce_pancreas_max_t = np.random.randint(16,60)
	ce_panc_vs_tum_max_hu = abs(ce_pancreas_max_hu - np.random.randint(30,80))  
	ce_panc_vs_tum_max_t = ce_pancreas_max_t - np.random.randint(-2,2)

	ct_date = randrange(10) < 3 and random_date(d1,d2) or 'NA'  
	if not ct_date == 'NA':
		ct_date_abs = ct_date - zerotime
		ct_date = ct_date.strftime("%d-%m-%y")
		ct_aorta_max_hu = np.random.normal(300,40)
		ct_aorta_max_t = 25
		ct_pancreas_max_t = np.random.randint(0,2) and 40 or 60
		ct_pancreas_max_hu = ct_pancreas_max_t==40 and ct_aorta_max_hu*(0.3+0.5*np.random.random()) or ct_aorta_max_hu*(0.2+0.4*np.random.random()) - (atrophy==1 and np.random.randint(10,30)) - (lipomatosis==1 and np.random.randint(10,30))

		ct_panc_vs_tum_max_hu = np.random.randint(0,1)
		ct_panc_vs_tum_max_t = ct_pancreas_max_t
	else:
		ct_date_abs = 'NA'
		ct_aorta_max_hu = 'NA'
		ct_aorta_max_t = 'NA'
		ct_pancreas_max_hu = 'NA'
		ct_pancreas_max_t = 'NA'
		ct_panc_vs_tum_max_hu = 'NA'
		ct_panc_vs_tum_max_t = 'NA'
	
	tumor_size = diagnosis==2 and np.random.poisson(25) or 10
	print tumor_size,tumor_size/20.
	pct_tumor = np.random.binomial(1,tumor_size/20.<1 and tumor_size/20. or 1)
	ct_tumor = np.random.binomial(1,tumor_size/30.<1 and tumor_size/40. or 1)
	print tumor_size,pct_tumor, tumor_size/60.<1 or 1
	line=[patient_id,
			gender,
			age,
			diagnosis,
			chemo,
			chemo_date.strftime("%d-%m-%y"),
			radio,
			radio_date.strftime("%d-%m-%y"),
			conc_elevation,
			exam_id,
			exam_date.strftime("%d-%m-%y"),
			exam_date_abs,
			ct_date,
			ct_date_abs,
			ct_aorta_max_hu,
			ct_aorta_max_t,
			ct_pancreas_max_hu,
			ct_pancreas_max_t,
			ct_panc_vs_tum_max_hu,
			ct_panc_vs_tum_max_t,
			atrophy,
			lipomatosis,
			ce_aorta_max_hu,
			ce_aorta_max_t,
			ce_pancreas_max_hu,
			ce_pancreas_max_t,
			ce_panc_vs_tum_max_hu,
			ce_panc_vs_tum_max_t,
			tumor_size,
			pct_tumor,
			ct_tumor
			]
	outline=[]
	for i in line:
		if not type(i)==str and not type(i)==timedelta:
			outline+=[int(i)]
		else:
			outline+=[i]
	
	return outline



first_line=['patient_id',
		'gender',
		'age',
		'diagnosis',
		'chemo',
		'chemo_date',
		'radio',
		'radio_date',
		'conc_elevation',
		'exam_id',
		'exam_date',
		'exam_date_abs',
		'ct_date',
		'ct_date_abs',
		'ct_aorta_max_hu',
		'ct_aorta_max_t',
		'ct_pancreas_max_hu',
		'ct_pancreas_max_t',
		'ct_panc_vs_tum_max_hu',
		'ct_panc_vs_tum_max_t',
		'atrophy',
		'lipomatosis',
		'ce_aorta_max_hu',
		'ce_aorta_max_t',
		'ce_pancreas_max_hu',
		'ce_pancreas_max_t',
		'ce_panc_vs_tum_max_hu',
		'ce_panc_vs_tum_max_t',
		'tumor_size',
		'pct_tumor',
		'ct_tumor'
		]

out_file.write(';'.join(map(str,first_line))+'\n')
for i in range(100):
	
	out_file.write(';'.join(map(str,make_line()))+'\n')