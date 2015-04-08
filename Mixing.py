from numpy import *
from pylab import *
import random

# grid size
x=60 #dimension along the x axis
y=40 #dimension along the y axis
k=8   #the exponent in the number of iterations
N=(10**k)   #number of iterations        #by changing N here, we might sample different "time intervals"
mid=int(y/2)

# generating the grid
a=zeros((x,y))    #defining the grid

density_1=[]      #mean density along the x axis of the gas A at the last time step
density_2=[]      #mean density along the x axis of the gas B at the last time step
density_3=[]	  #mean density along the x axis of the gas A at the intermediate time step
density_4=[]      #mean density along the x axis of the gas B at the intermedaite time step
density_5=[]      #mean density along the x axis of the gas A at the early time step 
density_6=[]      #mean density along the x axis of the gas B at the early time step
density_7=[]      #actual density along x axis for y/2,for gas A, at the last time step
density_8=[]      #actual density along x axis for y/2,for gas B, at the last time step

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
		print "bye"
        	for i in range (0,x):
            		count_1=0.0     
            		count_2=0.0
			if a[i,mid]==1:
				density_7.append(1) 
				density_8.append(0)
			elif a[i,mid]==2:
				density_7.append(0)
				density_8.append(1)
			else:
				density_7.append(0)
				density_8.append(0)

            		for j in range (0,y):
                		if a[i,j] == 1:
                    			count_1=count_1+1   #counting number of A particles at fixed x
                		if a[i,j] == 2:
                    			count_2=count_2+1   #counting number of B particles at fixed x
            		density_1.append(count_1/float(y))  #averaging over y
            		density_2.append(count_2/float(y))  #averaging over y
        	print a
		x_1=[]   #to store the x coordinates of the gas A at the end time
		y_1=[]   #to store the y coordinates of the gas A at the end time
		x_2=[]   #to store the x coordinates of the gas B at the end time
		y_2=[]   #to store the y coordinates of the gas B at the end time
		for i in range(0,x):
    			for j in range(0,y):
       				if a[i,j] == 1:
            				x_1.append(i)
            				y_1.append(j)
        			if a[i,j] == 2:
            				x_2.append(i)
            				y_2.append(j)

	if z == 7.5*(10**(k-1)): #finding the densities at an intermediate time
		print "hi again"
        	for i in range (0,x):
            		count_1=0.0     
            		count_2=0.0
            		for j in range (0,y):
                		if a[i,j] == 1:
                    			count_1=count_1+1   #counting number of A particles at fixed x
                		if a[i,j] == 2:
                    			count_2=count_2+1   #counting number of B particles at fixed x
            		density_3.append(count_1/float(y))  #averaging over y
            		density_4.append(count_2/float(y))  #averaging over y
        	print a
		x_3=[]   #to store the x coordinates of the gas A at the intermediate time
		y_3=[]   #to store the y coordinates of the gas A at the intermediate time
		x_4=[]   #to store the x coordinates of the gas B at the intermediate time
		y_4=[]   #to store the y coordinates of the gas B at the intermediate time
		for i in range(0,x):
    			for j in range(0,y):
       				if a[i,j] == 1:
            				x_3.append(i)
            				y_3.append(j)
        			if a[i,j] == 2:
            				x_4.append(i)
            				y_4.append(j)		

	if z == 4.5*(10**(k-1)): #finding the densities at an earlier time
		print "hi"
        	for i in range (0,x):
            		count_1=0.0     
            		count_2=0.0
            		for j in range (0,y):
                		if a[i,j] == 1:
                    			count_1=count_1+1   #counting number of A particles at fixed x
                		if a[i,j] == 2:
                    			count_2=count_2+1   #counting number of B particles at fixed x
            		density_5.append(count_1/float(y))  #averaging over y
            		density_6.append(count_2/float(y))  #averaging over y
        	print a
		x_5=[]   #to store the x coordinates of the gas A at the early time
		y_5=[]   #to store the y coordinates of the gas A at the early time
		x_6=[]   #to store the x coordinates of the gas B at the early time
		y_6=[]   #to store the y coordinates of the gas B at the early time
		for i in range(0,x):
    			for j in range(0,y):
       				if a[i,j] == 1:
            				x_5.append(i)
            				y_5.append(j)
        			if a[i,j] == 2:
            				x_6.append(i)
            				y_6.append(j)

print density_1,density_2
plot(density_1,'r-',label="Gas A, 10^8 -2 iterations")
plot(density_2,'b-',label="Gas B, 10^8 -2 iterations")
#plot(density_3,'r--',label="Gas A, 7.5*10^7 iterations")
#plot(density_4,'b--',label="Gas B, 7.5*10^7 iterations")
#plot(density_5, 'r*-',label="Gas A, 4.5*10^7 iterations")
#plot(density_6, 'b*-',label="Gas B, 4.5*10^7 iterations")
xlabel('Points along X axis')
ylabel('Number of particles (averaged over y axis)')
title("Density profile of the gases at different times")
legend(bbox_to_anchor=(1.0, 1.016),bbox_transform=plt.gcf().transFigure)
show()
#print a		

plot(density_7,'r*-',label="Gas A, 10^8 -2 iterations")
plot(density_8,'b*-',label="Gas B, 10^8 -2 iterations")
xlabel('Points along X axis')
ylabel('Number of particles of each Gas')
title('Variation of density in the middle of the grid, over all values of x')
legend(bbox_to_anchor=(1.0, 1.010),bbox_transform=plt.gcf().transFigure)
show()


plot(x_1,y_1,'or')
plot(x_2,y_2,'*b')
xlim(-10,(x+10))
ylim(-10,(y+10))
xlabel('X axis of grid')
ylabel('Y axis of grid')
title("Gas mixing at the end time. Red dots-> Gas A; Blue dots-> Gas B")
show()

plot(x_3,y_3,'or')
plot(x_4,y_4,'*b')
xlim(-10,(x+10))
ylim(-10,(y+10))
xlabel('X axis of grid')
ylabel('Y axis of grid')
title("Gas mixing at the intermediate time. Red dots-> Gas A; Blue dots-> Gas B")
show()

plot(x_5,y_5,'or')
plot(x_6,y_6,'*b')
xlim(-10,(x+10))
ylim(-10,(y+10))
xlabel('X axis of grid')
ylabel('Y axis of grid')
title("Gas mixing at the early time. Red dots-> Gas A; Blue dots-> Gas B")
show()



