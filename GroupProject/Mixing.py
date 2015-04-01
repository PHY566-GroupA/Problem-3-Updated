from numpy import *
from pylab import *
import random

# grid size
x=60 #dimension along the x axis
y=40 #dimension along the y axis
N=10**8   #number of iterations        #by changing N here, we can sample different "time intervals"

# generating the grid
a=zeros((x,y))

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
		r=random.random()  #choose random probability  
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
		r=random.random()  #choose random probability  
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
		r=random.random()  #choose random probability  
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
		r=random.random()  #choose random probability  
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
		r=random.random()  #choose random probability  
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
		r=random.random()  #choose random probability  
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
		r=random.random()  #choose random probability  
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
		r=random.random()  #choose random probability  
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
		r=random.random()  #choose random probability 
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
			else:   #move the particle down
				a[i,j+1]=a[i,j]
				a[i,j]=0.0

		else:                      #initiate to move right
			if a[i+1,j]!=0:   #break from while loop if (i+1,j) is occupied
				break		
			else:   #move the particle up
				a[i+1,j]=a[i,j]
				a[i,j]=0.0

print a		









