from pylab import *
import random
from itertools import groupby

#this code uses the central limit theorem to generate the gaussian distribution from the uniform distribution by taking averages from N number of samples of uniform distribution

N=((10.0)**(6))  #number of samples to collect from
k=2*sqrt(3)        #uniform distribution between 0 and k

def findnumbers(N):  
	summ=0.0
	for i in range(int(N)):
		summ=summ+random.uniform(0,k)
	average=summ/(N)	
	return average     

numbers=[]  #stores the numbers in this array

total_numbers=2000  #total number of points taken to find the resulting probability distribution, each of which is an average of N random elements from a uniform distribution

for i in range(total_numbers):
	numbers.append(findnumbers(N))      #constructing the array of numbers of our average random variable

numbers1=[]
for i in range(total_numbers):
	numbers1.append((sqrt(N))*(numbers[i]-(k/2.0))) 

numbers1.sort()
numbers2=np.around(numbers1,decimals=1)   #numbers2 has the sorted values upto oney decimal place

numbers3=[len(list(group)) for key, group in groupby(numbers2)]   #numbers3 has the number frequencies
print numbers3

numbers4=[]
for i in range(len(numbers3)):
	numbers4.append((10.0/(total_numbers))*numbers3[i])
	
numbers5=np.unique(numbers2)   #the distinct values in numbers2

x=[]
for i in range(-500,500):
	x.append(i/100.0)

gaussian=[] 
for i in range(len(x)):
	gaussian.append((1.0/(sqrt(2*pi)))*exp(-0.5*x[i]*x[i]))

plot(numbers5,numbers4,'r-')
plot(x,gaussian,'g-')
ylabel('Probability')
xlabel('Variable')
title('Comparison of ideal gaussian and the distribution of averages')
grid()
show()
