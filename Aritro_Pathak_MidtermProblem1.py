from pylab import *
#plots the equipotential lines, the V(r) of the first part, also the figure 8 in the report


initial_iterations=100   # the number of iterations after which the convergence criterion should be applied
charge=1.0 # (Q/epsilon_{0})*(unit grid area)
R=10
N=20   #can change the number of grid points from here
tolerance= 5*(10**(-6))  #can change the tolerance from here
x=linspace(-R,R,N)     #array of x coordinates
y=linspace(-R,R,N)	#array of y coordinates
V1=zeros(shape=(N,N))   
V=array(V1,dtype=float)    #initialising the potential to 0, initially.... The first coordinate of V gives the y coordinate and the 2nd coordinate gives the x coordinate. This is done so because later while doingthe contour plot, meshgrid does exactly the same thing with its grid.

a_1=0
a_2=0
b_1=0
b_2=0
for i in range(len(x)):
	if x[i]<-0.3 and x[i+1]>-0.3:
		a_1=i        # we will put the negative charge at -0.3 at this point.
		a_2=(i+1)    
	if x[i]<0.3 and x[i+1]>0.3:
		b_1=i          
		b_2=(i+1)    # we will put the positive charge at +0.3 at this point

def radial(a,b):		#gives the radial distance from origin of the particular point
	var1=sqrt(a*a+b*b)
	return var1

def distance1(a,b):		#gives the distance of a point from the negative charge
	var2=sqrt((a+0.3)**2+b**2)
	return var2

def distance2(a,b):		#gives the distance of a point from the positive charge
	var3=sqrt((a-0.3)**2+b**2)
	return var3

def average_array(X):		#gives the average of the absolute value of changes between successive arrays
	summing=0.0
	for i in range(N):
		for j in range(N):
			summing=summing+abs(X[i][j])
	variable= summing/(N*N)
	return variable

initial_average=0.0	
list_of_averages=[]  #will store all the differences of average values here
list_of_averages.append(initial_average)   #adding values to the list of averages
iterations=0  # number of iterations required

for m in range(initial_iterations):
	iterations+=1
	temp1=zeros(shape=(N,N))
	temp=array(temp1,dtype=float)
	for i in range(N):
		for j in range(N):
			if radial(x[i],y[j])<R: #only points within the circle get updated. All other points outside remain 0 at all times.
				if i==a_1 and j==int(0.5*(N-1)):
					temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]-charge)	
				elif i==b_2 and j==int(0.5*(N-1)):
					temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]+charge)
				else:
					temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i])
	list_of_averages.append(average_array(temp-V))
	V=temp  # assigning V to the values in temp in this iteration step 

	
while abs(list_of_averages[-1])>tolerance:
	iterations+=1		
	temp1=zeros(shape=(N,N))
	temp=array(temp1,dtype=float)
	for i in range(N):
		for j in range(N):
			if radial(x[i],y[j])<R: #only points within the circle get updated. All other points outside remain 0 at all times.
				if i==a_1 and j==int(0.5*(N-1)):
					temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]-charge)	 #implementing the jacobi algorithm here and below
				elif i==b_2 and j==int(0.5*(N-1)):
					temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]+charge)
				else:
					temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i])
	list_of_averages.append(average_array(temp-V))
	V=temp  # assigning V to the values in temp in this iteration step 

X,Y=meshgrid(x,y)

figure()       #plot of equipotential lines from my Jacobi simulation
CP1=contour(X,Y,V,50)
clabel(CP1,inline=False,fontsize=10)
title('Equipotential lines for Jacobi algorithm')
xlabel('x(m)')
ylabel('y(m)')
grid()
show()	

dipole_field1=zeros(shape=(N,N))   #field due to a couple of infinite line charge in a plane perpendicular to the line charge, placed at the location of the two charges
dipole_field2=array(dipole_field1,dtype=float)
for i in range(N):
	for j in range(N):
		if distance1(x[i],y[j])>0 and distance1(x[i],y[j])>0:
			dipole_field2[j][i]=1/(2*pi)*(log(distance1(x[i],y[j]))-log(distance2(x[i],y[j])))

dipole_field3=zeros(shape=(N,N))   #field due to a point dipole in a plane containing the dipole vector. We are ignoring higher order terms which should ideally come into the formula becausethis is not a point dipole.
dipole_field4=array(dipole_field3,dtype=float)
for i in range (N):
	for j in range(N):
		if distance1(x[i],y[j])>0 and distance1(x[i],y[j])>0:
			dipole_field4[j][i]=(0.6/(4*pi))*(x[i]/((radial(x[i],y[j]))**3))


figure()
CP2=contour(X,Y,dipole_field2,50) #equipotential lines due to couple of infinite line charges
clabel(CP2,inline=False,fontsize=10)
title('Equipotential lines for infinite line charge')
xlabel('x(m)')
ylabel('y(m)')
grid()
show()

#figure()
#CP3=contour(X,Y,dipole_field4,100) #equipotential lines due to point dipole)
#clabel(CP3,inline=True,fontsize=10)
#title('Equipotential lines for point dipole')
#xlabel('x(m)')
#ylabel('y(m)')
#show()

mysimulation_V=[]  #to plot the variation of the potential on the x axis due to Jacobi Algorithm
dipole_V1=[]		# plot the variation of potential due to the 2 infinite line charges
dipole_V2=[]		#plot the variation of potential due to the point dipole

for i in range(len(x)):   #to put in the potential values on the x axis
	mysimulation_V.append(V[int(0.5*(N-1))][i]) 
	dipole_V1.append(dipole_field2[int(0.5*(N-1))][i])
	dipole_V2.append(dipole_field4[int(0.5*(N-1))][i])

plot(x,mysimulation_V,'r-',label="Jacobi Algorithm")
plot(x,dipole_V1,'g-',label="Infinite line charge")
plot(x,dipole_V2,'b-',label="Point dipole")
xlabel('x(m)')
ylabel('Potential')
title('Variation of potential along X axis')
legend(loc="upper right")
grid()
show()
			
print "the number of iterations required for this run is: %d ." % iterations
#print a_1,a_2,b_1,b_2



 #plotting the iterations vs grid density obtained from codes 3 and 4 in this code itself

density=[60,70,80,90,100,110,120,130]

#tolerance for the Jacobi algorithm:5*(10^(-6))
#array for the iteration values for the Jacobi case
iterations_Jacobi=[3005,3832,4713,5641,6620,7620,8644,9684]

#tolerance for the SOR method: 5*(10^(-6))
#array for the iteration values for the SOR case
iterations_SOR=[1219,1359,1444,1482,1494,2088,2097,2099]

plot(density,iterations_Jacobi,'g-^',label='Jacobi')
plot(density,iterations_SOR,'r-^',label='SOR')
xlabel('Number of grid points in either x or y direction')
ylabel('Iterations')
title("Variation of Iterations with grid density in Jacobi algorithm and SOR algorithm with accuracy of 5*10^(-6)")
legend(loc="upper left")
grid()
show()




	
