from random import randrange
import numpy as np

nrows = 15
ncolumns = 10

a = np.array([[randrange(1, 20) for i in range(ncolumns)] for k in range(nrows)])
print(a)

avr = np.average(a, 1)
temp = np.copy(a)
ind_sorted = np.argsort(avr)

for i in range(nrows):
	a[i] = temp[ind_sorted[i]]

avr.sort()

for i in range(nrows):
	print(avr[i], end=' :\t')
	for j in range(ncolumns):
		print(a[i][j], end="\t")
	print()
