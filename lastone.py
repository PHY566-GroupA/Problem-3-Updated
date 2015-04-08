from pylab import *

a=[1,3,5,6,7,8,9,12,15,17,19,20]
for i in range(len(a)):
	if a[i]<13:
		print i
		continue
	else:
		break


