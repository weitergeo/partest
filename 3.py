import numpy as np
import csv
data1 = list(csv.reader(open('Tt1.csv')))
data2 = list(csv.reader(open('Tt2.csv')))

data3 = np.array(data1, dtype=float) + np.array(data2, dtype=float)
#data3 = data1 + data2
print data3
#print data2
