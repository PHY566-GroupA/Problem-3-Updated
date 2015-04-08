from pylab import *

C=8.0/(4.0*pi) #constant prefactor for calculating the fields
lim=0.50 # extreme limit of either the x or y coordinate in each side of the current loop
step=0.01 # length of discrete steps in which each current carrying side has been broken into

side1_y=[-lim+step*i for i in range(int(2*(lim/step)))] #array for the y position coordinates for the 1st side
x_1=0.500 # x coorinate of the first side

side2_x=[lim-step*i for i in range(int(2*(lim/step)))] #array for the x position coordinates for the 2nd side
y_2=0.500 # y coordinate for the 2nd side

side3_y=[lim-step*i for i in range(int(2*(lim/step)))] #array for the y position coordinates for the 3rd side
x_3=-0.500 #x coordinate for the 3rd side

side4_x=[-lim+step*i for i in range(int(2*(lim/step)))] #array for the x position coordinates for the 4th side
y_4=-0.500 #y coordinate for the 4th side

#part (a). finding the magnetic field on the z axis 

z_0=300 #half the number of steps on the z axis at which we want to find the magnetic field
z=[0.01*i for i in range(-z_0,z_0)]  #array of all the z coordinates of the z axis points
B_x=[0.0]*(2*z_0) 
B_y=[0.0]*(2*z_0)
B_z=[0.0]*(2*z_0)
for i in range(2*z_0):   #finding the fields at all points on the z axis
	for j in range(int(2*(lim/step))): #calculating the fields due to the 1st side
		B_x[i]=	B_x[i]+C*((step*z[i])/(sqrt(z[i]*z[i]+x_1*x_1+side1_y[j]*side1_y[j]))**3)
		B_y[i]= B_y[i]+0.0
		B_z[i]= B_z[i]+C*((step*x_1)/(sqrt(z[i]*z[i]+x_1*x_1+side1_y[j]*side1_y[j]))**3)

	for k in range(int(2*(lim/step))): #calculating the fields due to the 2nd side
		B_x[i]= B_x[i]+0.0
		B_y[i]= B_y[i]+C*((step*z[i])/(sqrt(z[i]*z[i]+y_2*y_2+side2_x[k]*side2_x[k]))**3)#the step increment is actually negative here
		B_z[i]= B_z[i]+C*((step*y_2)/(sqrt(z[i]*z[i]+y_2*y_2+side2_x[k]*side2_x[k]))**3) #'''''''''''''''''''''''''''''''''''''''

	for l in range(int(2*(lim/step))): #calculating the fields due to the 3rd side
		B_x[i]= B_x[i]+C*((-step*z[i])/(sqrt(z[i]*z[i]+x_3*x_3+side3_y[l]*side3_y[l]))**3)#the step increment is also actually negative here
		B_y[i]= B_y[i]+0.0
		B_z[i]= B_z[i]+C*((-step*x_3)/(sqrt(z[i]*z[i]+x_3*x_3+side3_y[l]*side3_y[l]))**3) #the step increment is also actually negative here

	for m in range(int(2*(lim/step))): #calculating the fields due to the 4th side
		B_x[i]= B_x[i]+0.0
		B_y[i]= B_y[i]+C*((-step*z[i])/(sqrt(z[i]*z[i]+y_4*y_4+side4_x[m]*side4_x[m]))**3) #the step increment is again back to being positive
		B_z[i]= B_z[i]+C*((-step*y_4)/(sqrt(z[i]*z[i]+y_4*y_4+side4_x[m]*side4_x[m]))**3)  #the step increment is again back to being positive

#plot(z,B_z)
#grid()
#show()

for i in range(len(B_x)):  #to eliminate the very small erro that python generates
	if B_x[i]<10**(-10):
		B_x[i]=0
for i in range(len(B_y)):  #to eliminate the very small error that python generates
	if B_y[i]<10**(-10):
		B_y[i]=0

R=sqrt(1.0/pi)
C_1=(8.0/2)*R*R
circularloop=[C_1/((R*R+z[i]*z[i])**1.50) for i in range(len(z))]
plot(z,circularloop,'g--',label="Circular loop field")
plot(z,B_z,'y-',label='Square loop field')
xlabel('Distance along Z axis(m)')
ylabel('Magnetic Field(Tesla)')
title('Magnetic Field on the axis of Circular loop and square loop with same area ')
legend(loc="upper right")
grid()
show()

plot(z,B_y,'g-')
xlabel('Distance along Z axis(m)')
ylabel('Y component of magnetic field(Tesla)')
title('Y component of magnetic field on the axis of square loop')
grid()
show()


#code for Parts (b) and (c). I'll write the general formula for the cross product, that would be less cumbersome.

#part (b)  z=1.0m, y=0.0m, as a function of x
x_max=300 #half the number of steps on the x axis at which we want to find the Magnetic field
x_array=[0.01*i for i in range(-x_max,x_max)]#array of all the x coordinates of the points on given line
B1_x=[0.0]*(2*x_max) #arrays storing the field values in this second case
B1_y=[0.0]*(2*x_max) #'''''''''''''''''''''''''''''''''''''''''''''''''''
B1_z=[0.0]*(2*x_max) #'''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(2*x_max):
	x=x_array[i]
	z=1.0
	y=0.0
	for j in range(int(2*(lim/step))): #calculating the fields due to the 1st side of square loop
		dz_=0.0
		dx_=0.0
		dy_=step
		x_=0.5
		z_=0.0
		y_=side1_y[j]			
		B1_x[i]= B1_x[i]+C*((dy_*(z-z_)-dz_*(y-y_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)	
		B1_y[i]= B1_y[i]+C*((dz_*(x-x_)-dx_*(z-z_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
		B1_z[i]= B1_z[i]+C*((dx_*(y-y_)-dy_*(x-x_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
	for k in range(int(2*(lim/step))): #calculating the fields due to the 2nd side of square loop
		dz_=0.0
		dy_=0.0
		dx_=-step
		z_=0.0
		y_=0.5
		x_=side2_x[k]
		B1_x[i]= B1_x[i]+C*((dy_*(z-z_)-dz_*(y-y_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)	
		B1_y[i]= B1_y[i]+C*((dz_*(x-x_)-dx_*(z-z_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
		B1_z[i]= B1_z[i]+C*((dx_*(y-y_)-dy_*(x-x_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
	for l in range(int(2*(lim/step))): #calculating the fields due to the 3rd side of square loop
		dz_=0.0
		dx_=0.0
		dy_=-step
		x_=-0.5		
		z_=0.0
		y_=side3_y[l]	
		B1_x[i]= B1_x[i]+C*((dy_*(z-z_)-dz_*(y-y_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)	
		B1_y[i]= B1_y[i]+C*((dz_*(x-x_)-dx_*(z-z_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
		B1_z[i]= B1_z[i]+C*((dx_*(y-y_)-dy_*(x-x_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
	for m in range(int(2*(lim/step))): #calculating the fields due to the 4th side of square loop
		dz_=0.0
		dy_=0.0
		dx_=step
		y_=-0.5
		z_=0.0
		x_=side4_x[m]
		B1_x[i]= B1_x[i]+C*((dy_*(z-z_)-dz_*(y-y_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)	
		B1_y[i]= B1_y[i]+C*((dz_*(x-x_)-dx_*(z-z_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
		B1_z[i]= B1_z[i]+C*((dx_*(y-y_)-dy_*(x-x_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
plot(x_array,B1_z,'r-')
xlabel('Distance along the X axis(m)')
ylabel('Z component of Magnetic Field (Tesla)')
title('Z component of magnetic field at z=1.0m, y=0.0m as a function of x')
grid()
show()
	
#part (c)  x=0.5m, y=0.0m, as a function of z
z_max=50 #half the number of steps on the z axis at which we want to find the Magnetic field
z_array=[0.01*i for i in range(-z_max,z_max)]#array of all the z coordinates of the points on given line
B2_x=[0.0]*(2*z_max) #arrays storing the field values in this second case
B2_y=[0.0]*(2*z_max) #'''''''''''''''''''''''''''''''''''''''''''''''''''
B2_z=[0.0]*(2*z_max) #'''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(2*z_max):
	z=z_array[i]
	x=0.50
	y=0.0
	for j in range(int(2*(lim/step))): #calculating the fields due to the 1st side of square loop
		dz_=0.0 # dz_ is used for the source variable, because dz' cannot be used
		dx_=0.0 # dx_ is used for the source variable, because dx' cannot be used
		dy_=step #...............................................................
		x_=0.5   #...............................................................
		z_=0.0   #...............................................................
		y_=side1_y[j]
		if ((x-x_)**2+(y-y_)**2+(z-z_)**2)==0:
			B2_x[i]=B2_x[i]+0.0
			B2_y[i]=B2_y[i]+0.0
			B2_z[i]=B2_z[i]+0.0			
		else:
			B2_x[i]= B2_x[i]+C*((dy_*(z-z_)-dz_*(y-y_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)	
			B2_y[i]= B2_y[i]+C*((dz_*(x-x_)-dx_*(z-z_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
			B2_z[i]= B2_z[i]+C*((dx_*(y-y_)-dy_*(x-x_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
	for k in range(int(2*(lim/step))): #calculating the fields due to the 2nd side of square loop
		dz_=0.0
		dy_=0.0
		dx_=-step
		z_=0.0
		y_=0.5
		x_=side2_x[k]
		B2_x[i]= B2_x[i]+C*((dy_*(z-z_)-dz_*(y-y_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)	
		B2_y[i]= B2_y[i]+C*((dz_*(x-x_)-dx_*(z-z_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
		B2_z[i]= B2_z[i]+C*((dx_*(y-y_)-dy_*(x-x_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
	for l in range(int(2*(lim/step))): #calculating the fields due to the 3rd side of square loop
		dz_=0.0
		dx_=0.0
		dy_=-step
		x_=-0.5		
		z_=0.0
		y_=side3_y[l]	
		B2_x[i]= B2_x[i]+C*((dy_*(z-z_)-dz_*(y-y_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)	
		B2_y[i]= B2_y[i]+C*((dz_*(x-x_)-dx_*(z-z_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
		B2_z[i]= B2_z[i]+C*((dx_*(y-y_)-dy_*(x-x_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
	for m in range(int(2*(lim/step))): #calculating the fields due to the 4th side of square loop
		dz_=0.0
		dy_=0.0
		dx_=step
		y_=-0.5
		z_=0.0
		x_=side4_x[m]
		B2_x[i]= B2_x[i]+C*((dy_*(z-z_)-dz_*(y-y_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)	
		B2_y[i]= B2_y[i]+C*((dz_*(x-x_)-dx_*(z-z_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)
		B2_z[i]= B2_z[i]+C*((dx_*(y-y_)-dy_*(x-x_))/((x-x_)**2+(y-y_)**2+(z-z_)**2)**1.5)

plot(z_array,B2_z,'r-')
xlabel('Distance along Z axis(m)')
ylabel('Z component of Magnetic Field(Tesla)')
title('Z component of magnetic field at x=0.5m, y=0.0m as a function of z')
grid()
show()





