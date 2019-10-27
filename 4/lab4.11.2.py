import numpy as np
from math import sqrt

def get_sum_of_divisors(num):
	sum = 1
	dlim = sqrt(num)
	d = 2
	while(d <= dlim):
		if(num % d == 0):
			sum += d
			if(d != num / d):
				sum += num/d
		d += 1
	return int(sum)


a = np.array([i+2 for i in range(27)])
b = np.copy(a)

for i in range(27):
	sum = get_sum_of_divisors(b[i])
	if(sum != b[i]):
		b[i] = sum

print("source\tchanged")
for i in range(27):
	print(a[i], end='\t')
	print(b[i])
