import numpy as np
import os

OUTPUT_DIR = '/home/denest/DISSER/R/data/'
output_csv = 'aorta_dens.csv'
aorta_file = open(os.path.join(OUTPUT_DIR, output_csv), 'w')

timeline = range(10, 32, 2) + range(38, 60, 4) + [90] + [180] + [300]

aorta = np.random.normal(np.random.randint(80, 190), 10, len(timeline))
pancreas = np.random.normal(np.random.randint(60, 110), 15, len(timeline))
tumor = np.random.normal(np.random.randint(30, 60), 5, len(timeline))

output_dict = {'aorta': aorta, 'pancreas': pancreas, 'tumor': tumor}

header = 'patient;exam;%s\n' % (';'.join(map(str, timeline)))
aorta_file.write(header)
for i in range(125):
    patient = np.random.randint(0, 100)
    exam = np.random.randint(0, 190)
    densities = np.round(np.random.normal(np.random.randint(80, 190), 10, len(timeline)), 0)
    aorta_file.write('%s;%s;%s\n' % (patient, exam, ';'.join(map(str, densities))))


# print ['_%s,'%(k).join(map(str,np.round(v,0))) for k,v in output_dict.items()]
# print [','.join(map(str,np.round(v,0))) for k,v in output_dict.items()]


