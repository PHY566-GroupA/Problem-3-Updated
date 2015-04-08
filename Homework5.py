from pylab import *
import random
from itertools import groupby
import math

random_numbers=[]   #list of all the random numbers
N=1000000  # total number of random numbers used. 
k=1.0   # the length from 0 till k would be used to generate random numbers
number_of_subdivisions=101  #number of divisions of the length 0.0 to 1.0. if we require 20 subdivisions, the total number of points would be 21. Change the number of subdivisions here

for i in range(N):
	random_numbers.append(random.uniform(0,k))

division=linspace(0.0,k,number_of_subdivisions)  #array of division points
frequency=zeros(number_of_subdivisions)          #number of random numbers at a particular place in the        
dl=k/(number_of_subdivisions-1)                      #interval between two points, the -1 is necessary

for i in range(len(random_numbers)):
	for j in range(len(division)):
		if (division[j]+dl)>random_numbers[i]:
			frequency[j]+=1
			break
probability=(frequency/float(N))/dl 

division1=delete(division,-1)
probability1=delete(probability,-1)
  
plot(division1,probability1)
xlabel('Random Variable')
ylabel('Probability')
ylim([0,1.1])
title('Uniform Probability distribution with 100 subdivisions, N=1000000')   # changed the title here with different number of subdivisions
grid()
show()

#generates a separate plot showing the distribution of numbers in the uniform distribution
x = np.random.uniform(0,k,N)
Bins = number_of_subdivisions
y=hist(x,Bins,color='blue')
plt.show()


summ=(sum(probability))*dl   #sums all the elements in the array probability
#print probability
print "The sum of all the probabilities for the uniform distribution is: %0.1f" %summ  #should print out 1.0


#plotting the gaussian

number_of_subdivisions=101  #also change the number of sub divisons here
random_gaussian1=[]     #stores the numbers in one of the axes
random_gaussian2=[]     #stores the numbers of the other axis

for i in range(N):
	u_1=random.uniform(0.0,1.0)   #implementing the Box Muller algorithm
	u_2=random.uniform(0.0,1.0)
	random_gaussian1.append(sqrt(-2*log(u_1))*cos(2*pi*u_2))
	random_gaussian2.append(sqrt(-2*log(u_1))*sin(2*pi*u_2))

frequency1=zeros(number_of_subdivisions) 
frequency2=zeros(number_of_subdivisions)
division=linspace(-6.0,6.0,number_of_subdivisions)    
dl=12.0/(number_of_subdivisions-1)   #number of subdivisions

for i in range(len(random_gaussian1)):
	for j in range(len(division)):
		if (division[j]+dl)>random_gaussian1[i]:
			frequency1[j]+=1
			break

for i in range(len(random_gaussian2)):
	for j in range(len(division)):
		if (division[j]+dl)>random_gaussian2[i]:
			frequency2[j]+=1
			break

probability_11=(frequency1/float(N))/dl
probability_22=(frequency2/float(N))/dl

summ1=(sum(probability_11))*dl
summ2=(sum(probability_22))*dl
print "The sum of probabilities in the case of the two Gaussians is: % 0.1f, %0.1f" % (summ1, summ2)   #should print out 1.0 and 1.0
print frequency1
print frequency2

mu=0.0
sigma=1.0
x=linspace(-6,6,201)

plot(division,probability_11,'r-',label="Gaussian Random")
plot(x,mlab.normpdf(x,mu,sigma),'g-',label="Ideal Gaussian")
xlabel('Random Variable')
ylabel('Probability')
title('Gaussian Probability distribution with 100 subdivisions,N=1000000 first case')
legend(loc="upper right")
grid()
show()

plot(division,probability_22,'r-',label="Gaussian Random")
plot(x,mlab.normpdf(x,mu,sigma),'g-',label="Ideal Gaussian")
xlabel('Random Variable')
ylabel('Probability')
title('Gaussian Probability distribution with 100 subdivisions,N=1000000 second case')
legend(loc="upper right")
grid()
show()
		
	




							
			




