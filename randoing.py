from pylab import *
import random

N=5*((10.0)**(4))  #number of samples to collect from
k=5.0        #uniform distribution between 0 and k
subdivisions=100 # divide the interval between 0 and k into 'subdivision' number of intervals

def findnumbers(N):  
	summ=0.0
	for i in range(int(N)):
		summ=summ+random.uniform(0,k)

	average=summ/(N)	
	return (sqrt(N))*(average-(k/2.0))     

numbers=[]  #stores the numbers in this array

total_numbers=1000  #total number of points taken to find the resulting probability distribution

for i in range(total_numbers):
	numbers.append(findnumbers(N))      #constructing the array of numbers of our average random variable
print numbers

def frequency_dist(k,subdivisions,a):        #finding the frequency distribution in any array of numbers
	freq=[0.0]*subdivisions    
	length=k/subdivisions
	for j in range(len(a)):
		for i in range(int(-subdivisions/2.0),int(subdivisions/2.0)):  
			if (i*length)<a[j]:
				continue
			else:	
				freq[i]=freq[i]+1
				break
	return freq

frequency1=frequency_dist(k,subdivisions,numbers) #calling on the function frequency_dist to act on the array `numbers'

frequency=[0.0]*subdivisions

for i in range(subdivisions):
	frequency[i]=(1/N)*(frequency1[i]) 

 
x=[i*(k/(subdivisions)) for i in range(int(-subdivisions/2.0),int(subdivisions/2.0))]

plot(x,frequency)
xlabel('interval of uniform distribution')
ylabel('frequency distribution for the population')
title('population distribution')
grid()
show()


plot(x,frequency_dist(k,subdivisions,numbers))
xlabel('interval of uniform distribution')
ylabel('frequency distribution for the population')
title('population distribution')
grid()
show()


#plot(numbers)
#grid()
#show()

