from numpy import *
from pylab import *
import random

# grid size
x=60 #dimension along the x axis
y=40 #dimension along the y axis
k=8   #the exponent in the number of iterations
N=(10**k)   #number of iterations        #by changing N here, we can sample different "time intervals"
mid=int(y/2)
iteration_number=0
print "there will be 50 iterations"
# generating the grid
#a=zeros((x,y))    #defining the grid

density_1=[]      #mean density along the x axis of the gas A at the last time step
density_2=[]      #mean density along the x axis of the gas B at the last time step
density_3=[]	  #mean density along the x axis of the gas A at the intermediate time step
density_4=[]      #mean density along the x axis of the gas B at the intermediate time step
density_5=[]      #mean density along the x axis of the gas A at the early time step 
density_6=[]      #mean density along the x axis of the gas B at the early time step

for w in range(0,50):        #repeating for each of 50 steps
	iteration_number+=1
        print iteration_number    #to keep track of which iteration number we are in right now.
	temp_1=[]   #temporary array defined to store the densities and later appended to density_1
	temp_2=[]   #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''2
	temp_3=[]   #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''3
	temp_4=[]   #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''4
	temp_5=[]   #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''5
	temp_6=[]   #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''6
	a=zeros((x,y))  #define the grid
	# one-third of the grid to be filled with gas species 'A'
	for j in range(0,y):
	    for i in range(0,int(x/3)):
		a[i,j]=1.0      #gas species A corresponds to the number 1.0

	# one-third of the grid to be filled with gas species 'B'
	for j in range(0,y):
	    for i in range(int((2*x)/3),x):
		a[i,j]=2.0      #gas species B corresponds to the number 2.0

	for z in range(0,N):    #naming this dummy variable z 
		while True:                             # random selection of only occupied sites
			i=random.choice(range(0,x))
			j=random.choice(range(0,y))
			if a[i,j] == 0.0:                 # if the chosen site is empty, break out of the while loop 
				break
			elif i==0 and j==0:               # if the chosen site is filled, and it is the bottom left corner 
				r=random.random()  #to choose equal probability
				if 0.0<=r<=0.5:            #initiate to move right
					if a[i+1,j]!=0:   #break from while loop if (i+1,j) is occupied
						break		
					else:    #move the particle right               
						a[i+1,j]=a[i,j]
						a[i,j]=0.0       
		
				else:                      #initiate to move up
					if a[i,j+1]!=0:   #break from while loop if (i,j+1) is occupied
						break		
					else:   #move the particle up
						a[i,j+1]=a[i,j]
						a[i,j]=0.0

			elif i==(x-1) and j==0:               # if the chosen site is filled, and it is the bottom right corner 
				r=random.random()  #to choose equal probability  
				if 0.0<=r<=0.5:            #initiate to move left
					if a[i-1,j]!=0:   #break from while loop if (i-1,j) is occupied
						break		
					else:    #move the particle left               
						a[i-1,j]=a[i,j]
						a[i,j]=0.0       
		
				else:                      #initiate to move up
					if a[i,j+1]!=0:   #break from while loop if (i,j+1) is occupied
						break		
					else:   #move the particle up
						a[i,j+1]=a[i,j]
						a[i,j]=0.0

			elif i==(x-1) and j==(y-1):       # if the chosen site is filled, and it is the top right corner 
				r=random.random()  #to choose equal probability  
				if 0.0<=r<=0.5:            #initiate to move left
					if a[i-1,j]!=0:   #break from while loop if (i-1,j) is occupied
						break		
					else:    #move the particle left               
						a[i-1,j]=a[i,j]
						a[i,j]=0.0       
		
				else:                      #initiate to move down
					if a[i,j-1]!=0:   #break from while loop if (i,j-1) is occupied
						break		
					else:   #move the particle down
						a[i,j-1]=a[i,j]
						a[i,j]=0.0

			elif i==0 and j==(y-1):       # if the chosen site is filled, and it is the top left corner 
				r=random.random()  #to choose equal probability 
				if 0.0<=r<=0.5:            #initiate to move right
					if a[i+1,j]!=0:   #break from while loop if (i+1,j) is occupied
						break		
					else:    #move the particle right               
						a[i+1,j]=a[i,j]
						a[i,j]=0.0       
		
				else:                      #initiate to move down
					if a[i,j-1]!=0:   #break from while loop if (i,j-1) is occupied
						break		
					else:   #move the particle down
						a[i,j-1]=a[i,j]
						a[i,j]=0.0

			elif i==0:  #this is the left edge of the grid, excluding the two corners that have been taken care of
				r=random.random()  #to choose equal probability
				if 0.0<=r<=0.33:            #initiate to move right
					if a[i+1,j]!=0:   #break from while loop if (i+1,j) is occupied
						break		
					else:    #move the particle right               
						a[i+1,j]=a[i,j]
						a[i,j]=0.0       
		
				elif 0.33<r<=0.67:                      #initiate to move down
					if a[i,j-1]!=0:   #break from while loop if (i,j-1) is occupied
						break		
					else:   #move the particle down
						a[i,j-1]=a[i,j]
						a[i,j]=0.0
		
				else:                      #initiate to move up
					if a[i,j+1]!=0:   #break from while loop if (i,j+1) is occupied
						break		
					else:   #move the particle up
						a[i,j+1]=a[i,j]
						a[i,j]=0.0

			elif i==(x-1):  #this is the right edge of the grid, excluding the two corners that have been taken care of
				r=random.random()  #to choose equal probability 
				if 0.0<=r<=0.33:            #initiate to move left
					if a[i-1,j]!=0:   #break from while loop if (i-1,j) is occupied
						break		
					else:    #move the particle left               
						a[i-1,j]=a[i,j]
						a[i,j]=0.0       
		
				elif 0.33<r<=0.67:                      #initiate to move down
					if a[i,j-1]!=0:   #break from while loop if (i,j-1) is occupied
						break		
					else:   #move the particle down
						a[i,j-1]=a[i,j]
						a[i,j]=0.0
		
				else:                      #initiate to move up
					if a[i,j+1]!=0:   #break from while loop if (i,j+1) is occupied
						break		
					else:   #move the particle up
						a[i,j+1]=a[i,j]
						a[i,j]=0.0


			elif j==0:  #this is the bottom edge of the grid, excluding the two corners that have been taken care of
				r=random.random()  #to choose equal probability  
				if 0.0<=r<=0.33:            #initiate to move left
					if a[i-1,j]!=0:   #break from while loop if (i-1,j) is occupied
						break		
					else:    #move the particle left               
						a[i-1,j]=a[i,j]
						a[i,j]=0.0       
		
				elif 0.33<r<=0.67:                      #initiate to move up
					if a[i,j+1]!=0:   #break from while loop if (i,j+1) is occupied
						break		
					else:   #move the particle down
						a[i,j+1]=a[i,j]
						a[i,j]=0.0
		
				else:                      #initiate to move right
					if a[i+1,j]!=0:   #break from while loop if (i+1,j) is occupied
						break		
					else:   #move the particle up
						a[i+1,j]=a[i,j]
						a[i,j]=0.0


			elif j==(y-1):  #this is the upper edge of the grid, excluding the two corners that have been taken care of
				r=random.random()  #to choose equal probability  
				if 0.0<=r<=0.33:            #initiate to move left
					if a[i-1,j]!=0:   #break from while loop if (i-1,j) is occupied
						break		
					else:    #move the particle left               
						a[i-1,j]=a[i,j]
						a[i,j]=0.0       
		
				elif 0.33<r<=0.67:                      #initiate to move down
					if a[i,j-1]!=0:   #break from while loop if (i,j-1) is occupied
						break		
					else:   #move the particle down
						a[i,j-1]=a[i,j]
						a[i,j]=0.0
		
				else:                      #initiate to move right
					if a[i+1,j]!=0:   #break from while loop if (i+1,j) is occupied
						break		
					else:   #move the particle up
						a[i+1,j]=a[i,j]
						a[i,j]=0.0

			else:     #the chosen point lies in the interior
		
				r=random.random()  #to choose equal probability
				if 0.0<=r<=0.25:            #initiate to move left
					if a[i-1,j]!=0:   #break from while loop if (i-1,j) is occupied
						break		
					else:    #move the particle left               
						a[i-1,j]=a[i,j]
						a[i,j]=0.0 
				elif 0.25<r<=0.50:                      #initiate to move down
					if a[i,j-1]!=0:   #break from while loop if (i,j-1) is occupied
						break		
					else:   #move the particle down
						a[i,j-1]=a[i,j]
						a[i,j]=0.0

				elif 0.50<r<=0.75:                      #initiate to move up
					if a[i,j+1]!=0:   #break from while loop if (i,j+1) is occupied
						break		
					else:   #move the particle up
						a[i,j+1]=a[i,j]
						a[i,j]=0.0

				else:                      #initiate to move right
					if a[i+1,j]!=0:   #break from while loop if (i+1,j) is occupied
						break		
					else:   #move the particle right
						a[i+1,j]=a[i,j]
						a[i,j]=0.0

		if z == ((10**k)-2): #finding the densities at a time very close to the end of simulation
			print "final time"
			for i in range (0,x):
		    		count_1=0.0     
		    		count_2=0.0
		    		for j in range (0,y):
		        		if a[i,j] == 1:
		            			count_1=count_1+1   #counting number of A particles at fixed x
		        		if a[i,j] == 2:
		            			count_2=count_2+1   #counting number of B particles at fixed x
		    		temp_1.append(count_1/float(y))  #averaging over y
		    		temp_2.append(count_2/float(y))  #averaging over y
			
		if z == 7.5*(10**(k-1)): #finding the densities at an intermediate time
			print "intermediate time"
			for i in range (0,x):
		    		count_1=0.0     
		    		count_2=0.0
		    		for j in range (0,y):
		        		if a[i,j] == 1:
		            			count_1=count_1+1   #counting number of A particles at fixed x
		        		if a[i,j] == 2:
		            			count_2=count_2+1   #counting number of B particles at fixed x
		    		temp_3.append(count_1/float(y))  #averaging over y
		    		temp_4.append(count_2/float(y))  #averaging over y
					
		if z == 4.5*(10**(k-1)): #finding the densities at an earlier time
			print "early time"
			for i in range (0,x):
		    		count_1=0.0     
		    		count_2=0.0
		    		for j in range (0,y):
		        		if a[i,j] == 1:
		            			count_1=count_1+1   #counting number of A particles at fixed x
		        		if a[i,j] == 2:
		            			count_2=count_2+1   #counting number of B particles at fixed x
		    		temp_5.append(count_1/float(y))  #averaging over y
		    		temp_6.append(count_2/float(y))  #averaging over y
			
	density_1.append(temp_1)
	density_2.append(temp_2)
	density_3.append(temp_3)
	density_4.append(temp_4)
	density_5.append(temp_5)
	density_6.append(temp_6)

superdensity_1=[]   #stores the averages over the 50 steps
superdensity_2=[]   #''''''''''''''''''''''''''''''''''''''
superdensity_3=[]   #''''''''''''''''''''''''''''''''''''''
superdensity_4=[]   #''''''''''''''''''''''''''''''''''''''
superdensity_5=[]   #''''''''''''''''''''''''''''''''''''''
superdensity_6=[]   #''''''''''''''''''''''''''''''''''''''

for p in range(x):
	x_1=0.0
	x_2=0.0
	x_3=0.0
	x_4=0.0
	x_5=0.0
	x_6=0.0
	for q in range(50):
		x_1=x_1+density_1[q][p]    #adding over the 50 different runs
		x_2=x_2+density_2[q][p]    #''''''''''''''''''''''''''''''''''
		x_3=x_3+density_3[q][p]    #''''''''''''''''''''''''''''''''''
		x_4=x_4+density_4[q][p]    #''''''''''''''''''''''''''''''''''
		x_5=x_5+density_5[q][p]    #''''''''''''''''''''''''''''''''''
		x_6=x_6+density_6[q][p]    #''''''''''''''''''''''''''''''''''
	superdensity_1.append(x_1/50)
	superdensity_2.append(x_2/50)
	superdensity_3.append(x_3/50)
	superdensity_4.append(x_4/50)
	superdensity_5.append(x_5/50)
	superdensity_6.append(x_6/50)

print superdensity_1,superdensity_2
plot(superdensity_1,'r-',label="Gas A, 10^8 -2 iterations")
plot(superdensity_2,'b-',label="Gas B, 10^8 -2 iterations")
plot(superdensity_3,'r--',label="Gas A, 7.5*10^7 iterations")
plot(superdensity_4,'b--',label="Gas B, 7.5*10^7 iterations")
plot(superdensity_5, 'r*',label="Gas A, 4.5*10^7 iterations")
plot(superdensity_6, 'b*',label="Gas B, 4.5*10^7 iterations")
xlabel('Points along X axis')
ylabel('Number of particles (averaged over y axis)')
title("Density profile of the gases at different times")
legend(bbox_to_anchor=(1, 1.012),bbox_transform=plt.gcf().transFigure)
show()
#print a		









