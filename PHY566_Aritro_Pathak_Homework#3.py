from pylab import *

m=0.046     	# Mass in Kilograms
theta_1=pi/20  	#inital angles
theta_2=pi/12   #inital angles
theta_3=pi/6    #initial angles
theta_4=pi/4    #initial angles
C_1=0.5     	# Lower velocity drag coefficient
C_2=7.0         # Higher velocity drag coefficent
r=1.29      	# density of air
A=0.0014    	# Frontal area of golf ball
g=9.8       	# Acceleration due to gravity
dt=0.01     	# Time step
K=0.25     	# Magnus Force constant
X= (C_1*r*A)/m
Y= (C_2*r*A)/m
theta=[theta_1,theta_2,theta_3,theta_4]   #list of different initial angles

def dimple_drag_spin1(theta):
	x=[[],[],[],[]]   # 2 dimensional list keeping x values for theta_1, theta_2,theta_3,theta_4
	y=[[],[],[],[]]   # 2 dimensional list keeping y values for theta_1, theta_2,theta_3,theta_4
	v_x=[[],[],[],[]] # list of speed in x direction at each time step for theta_1, theta_2,theta_3,theta_4
	v_y=[[],[],[],[]] # list of speed in y direction at each time step for theta_1, theta_2,theta_3,theta_4

	for i in range(len(theta)):
		x[i].append(0.0)	#initial x coordinate for i'th angle
		y[i].append(0.0)        #initial y coordinate for i'th angle          
		v_x[i].append(70.0*cos(theta[i])) #initial velocity in x direction for i'th angle
		v_y[i].append(70.0*sin(theta[i])) #initial velocity in y direction for i'th angle
		k=0
 		while y[i][k]>=0 :
	
			x[i].append(x[i][k]+(v_x[i][k])*dt)      #update x coordinate
			y[i].append(y[i][k]+(v_y[i][k])*dt)      #update y coordinate
			if sqrt(v_x[i][k]**2 + v_y[i][k]**2) <= 14 :                                           # lower velocity 
				v_x[i].append(v_x[i][k]+dt*(-K*v_y[i][k]-X*(sqrt(v_x[i][k]**2 + v_y[i][k]**2))*v_x[i][k]))  #update v_x
				v_y[i].append(v_y[i][k]+dt*( K*v_x[i][k]-X*(sqrt(v_x[i][k]**2 + v_y[i][k]**2))*(v_y[i][k])-g))#update v_y
		
			else :  									  #higher velocity
				v_x[i].append(v_x[i][k]+dt*(-K*v_y[i][k]-Y*v_x[i][k]))  		 #update v_x
				v_y[i].append(v_y[i][k]+dt*(K*v_x[i][k]-g-Y*v_y[i][k]))  		 #update v_y
			k+=1
	return x,y   #return only the x and y values
		
def dimple_drag_spin2(theta):  #reversing the spin of the ball
	K=-0.25
	x=[[],[],[],[]]   # 2 dimensional list keeping x values for theta_1, theta_2,theta_3,theta_4
	y=[[],[],[],[]]   # 2 dimensional list keeping y values for theta_1, theta_2,theta_3,theta_4
	v_x=[[],[],[],[]] # list of speed in x direction at each time step for theta_1, theta_2,theta_3,theta_4
	v_y=[[],[],[],[]] # list of speed in y direction at each time step for theta_1, theta_2,theta_3,theta_4

	for i in range(len(theta)):
		x[i].append(0.0)	#initial x coordinate for i'th angle
		y[i].append(0.0)        #initial y coordinate for i'th angle          
		v_x[i].append(70.0*cos(theta[i])) #initial velocity in x direction for i'th angle
		v_y[i].append(70.0*sin(theta[i])) #initial velocity in y direction for i'th angle
		k=0
 		while y[i][k]>=0 :
	
			x[i].append(x[i][k]+(v_x[i][k])*dt)      #update x coordinate
			y[i].append(y[i][k]+(v_y[i][k])*dt)      #update y coordinate
			if sqrt(v_x[i][k]**2 + v_y[i][k]**2) <= 14 :                                           # lower velocity 
				v_x[i].append(v_x[i][k]+dt*(-K*v_y[i][k]-X*(sqrt(v_x[i][k]**2 + v_y[i][k]**2))*v_x[i][k]))  #update v_x
				v_y[i].append(v_y[i][k]+dt*( K*v_x[i][k]-X*(sqrt(v_x[i][k]**2 + v_y[i][k]**2))*(v_y[i][k])-g))#update v_y
		
			else :  									  #higher velocity
				v_x[i].append(v_x[i][k]+dt*(-K*v_y[i][k]-Y*v_x[i][k]))  		 #update v_x
				v_y[i].append(v_y[i][k]+dt*(K*v_x[i][k]-g-Y*v_y[i][k]))  		 #update v_y
			k+=1
	return x,y  #return only the x and y values

def dimple_drag(theta):
	
	x=[[],[],[],[]]   # 2 dimensional list keeping x values for theta_1,theta_2,theta_3,theta_4
	y=[[],[],[],[]]   # 2 dimensional list keeping y values for theta_1,theta_2,theta_3,theta_4
	v_x=[[],[],[],[]] # list of speed in x direction at each time step for theta_1,theta_2,theta_3,theta_4
	v_y=[[],[],[],[]] # list of speed in y direction at each time step for theta_1,theta_2,theta_3,theta_4

	for i in range(len(theta)):
		x[i].append(0.0)	#initial x coordinate for i'th angle
		y[i].append(0.0)        #initial y coordinate for i'th angle          
		v_x[i].append(70.0*cos(theta[i])) #initial velocity in x direction for i'th angle
		v_y[i].append(70.0*sin(theta[i])) #initial velocity in y direction for i'th angle
		k=0
 		while y[i][k]>=0 :
	
			x[i].append(x[i][k]+(v_x[i][k])*dt)      #update x coordinate
			y[i].append(y[i][k]+(v_y[i][k])*dt)      #update y coordinate
			if sqrt(v_x[i][k]**2 + v_y[i][k]**2) <= 14 :                                           # lower velocity 
				v_x[i].append(v_x[i][k]+dt*(-X*(sqrt(v_x[i][k]**2 + v_y[i][k]**2))*v_x[i][k]))  #update v_x
				v_y[i].append(v_y[i][k]+dt*(-X*(sqrt(v_x[i][k]**2 + v_y[i][k]**2))*(v_y[i][k])-g))#update v_y
		
			else :  									  #higher velocity
				v_x[i].append(v_x[i][k]+dt*(-Y*v_x[i][k]))  		 #update v_x
				v_y[i].append(v_y[i][k]+dt*(-g-Y*v_y[i][k]))  		 #update v_y
			k+=1
	return x,y   #return only the x and y values
	
def smooth_drag(theta):
	x=[[],[],[],[]]   # 2 dimensional list keeping x values for theta_1,theta_2,theta_3,theta_4
	y=[[],[],[],[]]   # 2 dimensional list keeping y values for theta_1,theta_2,theta_3,theta_4
	v_x=[[],[],[],[]] # list of speed in x direction at each time step for theta_1,theta_2,theta_3,theta_4
	v_y=[[],[],[],[]] # list of speed in y direction at each time step for theta_1,theta_2,theta_3,theta_4

	for i in range(len(theta)):
		x[i].append(0.0)	#initial x coordinate for i'th angle
		y[i].append(0.0)        #initial y coordinate for i'th angle          
		v_x[i].append(70.0*cos(theta[i])) #initial velocity in x direction for i'th angle
		v_y[i].append(70.0*sin(theta[i])) #initial velocity in y direction for i'th angle
		k=0
 		while y[i][k]>=0 :
	
			x[i].append(x[i][k]+(v_x[i][k])*dt)    #update x coordinate
			y[i].append(y[i][k]+(v_y[i][k])*dt)    #update y coordinate
			v_x[i].append(v_x[i][k]+dt*(-X*(sqrt(v_x[i][k]**2 + v_y[i][k]**2))*v_x[i][k]))  #update v_x
			v_y[i].append(v_y[i][k]+dt*(-X*(sqrt(v_x[i][k]**2 + v_y[i][k]**2))*(v_y[i][k])-g))#update v_y
			k+=1
	return x,y   #return only the x and y values

def ideal_trajectory(theta):
	x=[[],[],[],[]]   # 2 dimensional list keeping x values for theta_1,theta_2,theta_3,theta_4
	y=[[],[],[],[]]   # 2 dimensional list keeping y values for theta_1,theta_2,theta_3,theta_4
	v_x=[[],[],[],[]] # list of speed in x direction at each time step for theta_1,theta_2,theta_3,theta_4
	v_y=[[],[],[],[]] # list of speed in y direction at each time step for theta_1,theta_2,theta_3,theta_4

	for i in range(len(theta)):
		x[i].append(0.0)	#initial x coordinate for i'th angle
		y[i].append(0.0)        #initial y coordinate for i'th angle          
		v_x[i].append(70.0*cos(theta[i])) #initial velocity in x direction for i'th angle
		v_y[i].append(70.0*sin(theta[i])) #initial velocity in y direction for i'th angle
		k=0
 		while y[i][k]>=0 :
	
			x[i].append(x[i][k]+(v_x[i][k])*dt)    #update x coordinate
			y[i].append(y[i][k]+(v_y[i][k])*dt)    #update y coordinate
			v_x[i].append(v_x[i][k])  #update v_x
			v_y[i].append(v_y[i][k]-g*dt)#update v_y
			k+=1
	return x,y    #return only the x and y values

list1,list2= ideal_trajectory(theta) #assign coordinate lists for plotting later
list3,list4= smooth_drag(theta)      #''''''''''''''''''''''''''''''''''''''''''
list5,list6= dimple_drag(theta)      #''''''''''''''''''''''''''''''''''''''''''
list7,list8= dimple_drag_spin1(theta) # '''''''''''''''''''''''''''''''''''''''''
list9,list10=dimple_drag_spin2(theta) #''''''''''''''''''''''''''''''''''''''''''

plot(list1[0],list2[0],"r-",label="Initial:9 degree") #ideal trajectory 
plot(list1[1],list2[1],"b-",label="Initial:15 degree")
plot(list1[2],list2[2],"g-",label="Initial:30 degree")
plot(list1[3],list2[3],"y-",label="Initial:45 degree")
xlabel('x (meter)')
ylabel('y (meter)')
title('Ideal Trajectory for 4 different angles')
legend(bbox_to_anchor=(0.95, 0.9),bbox_transform=plt.gcf().transFigure)
axes().set_aspect('equal')
grid()
show()

plot(list3[0],list4[0],"r-",label="Initial:9 degree") #smooth golf ball with drag
plot(list3[1],list4[1],"b-",label="Initial:15 degree")
plot(list3[2],list4[2],"g-",label="Initial:30 degree")
plot(list3[3],list4[3],"y-",label="Initial:45 degree")
xlabel('x (meter)')
ylabel('y (meter)')
title('Smooth golf ball with drag')
legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
axes().set_aspect('equal')
grid()
show()

plot(list5[0],list6[0],"r-",label="Initial:9 degree") #dimpled golf ball with drag
plot(list5[1],list6[1],"b-",label="Initial:15 degree")
plot(list5[2],list6[2],"g-",label="Initial:30 degree")
plot(list5[3],list6[3],"y-",label="Initial:45 degree")
xlabel('x (meter)')
ylabel('y (meter)')
title('Dimpled golf ball with drag')

axes().set_aspect('equal')
grid()
show()

plot(list7[0],list8[0],"r-",label="Initial:9 degree") #dimpled ball with drag and spin with K=0.25
plot(list7[1],list8[1],"b-",label="Initial:15 degree")
plot(list7[2],list8[2],"g-",label="Initial:30 degree")
plot(list7[3],list8[3],"y-",label="Initial:45 degree")
xlabel('x (meter)')
ylabel('y (meter)')
title('Dimpled golf ball with drag and anticlockwise spin')
legend(bbox_to_anchor=(1, 1.015),bbox_transform=plt.gcf().transFigure)
axes().set_aspect('equal')
grid()
show()

plot(list9[0],list10[0],"r-",label="Initial:9 degree") #dimpled ball with drag and spin with K=-0.25
plot(list9[1],list10[1],"b-",label="Initial:15 degree")
plot(list9[2],list10[2],"g-",label="Initial:30 degree")
plot(list9[3],list10[3],"y-",label="Initial:45 degree")
xlabel('x (meter)')
ylabel('y (meter)')
title('Dimpled golf ball with drag and clockwise spin')
legend(bbox_to_anchor=(1, 1.012),bbox_transform=plt.gcf().transFigure)
axes().set_aspect('equal')
grid()
show()














