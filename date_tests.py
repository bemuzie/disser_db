from datetime import datetime
import re

test_data = ['12.2.13',':17.06.1954',': 17. 6.1954','1954']

for i in test_data:
	date_str ='-'.join([j for j in re.split('\D',i) if j])
	try:
		d=datetime.strptime(date_str, '%d-%m-%Y')
	except ValueError:
		try:
			d=datetime.strptime(date_str, '%d-%m-%y')
		except ValueError:	
			d=datetime.strptime(date_str, '%Y')
		
	print d
