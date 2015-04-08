from pylab import *

#part c
#Number of iterations in SOR method

#this code does not seem to converge when I take the parameter w greater than 1 in this code. I worked with a value of w=0.5
#the problem of having to take only N in multiples of 10 persisits here.

initial_iterations=10   # the number of iterations after which the convergence criterion should be applied, to avoid a possible false convergence
charge=1.0 # (Q/epsilon_{0})*(unit grid area)
R=10 #radius
grid=linspace(90,90,1)  #change the value of the number of grid points here.
iterations1=zeros(4)
iteration=array(iterations1,dtype=float)
tolerance= 5*(10**(-6))

def radial(a,b):   #calculates the radial distance from origin
	var1=sqrt(a*a+b*b)
	return var1

def distance1(a,b): #calculates distance from the negative charge
	var2=sqrt((a+0.3)**2+b**2)
	return var2

def distance2(a,b):  #calculates the distance from the positive charge
	var3=sqrt((a-0.3)**2+b**2)
	return var3


for p in range(len(grid)):
	initial_max=0.0	
	list_of_maxima=[]  #will store all the differences of average values here
	list_of_maxima.append(initial_max)
	p_1=int(grid[p])
	w=0.5  # optimum value
	x=linspace(-R,R,p_1)
	y=linspace(-R,R,p_1)
	V1=zeros(shape=(p_1,p_1))
	V=array(V1,dtype=float)    #initialising the potential to 0, initially.... The first coordinate of V gives the y coordinate and the 2nd coordinate gives the x coordinate. This is done so because later while doingthe contour plot, meshgrid does exactly the same thing with its own grids.
	for i in range(p_1):
		if x[i]<-0.3 and x[i+1]>-0.3:
			a_1=i        # we will put the negative charge at this location
			a_2=(i+1)    
		if x[i]<0.3 and x[i+1]>0.3:
			b_1=i        
			b_2=(i+1)    #we will put the positive charge at this location 
	
	it=0
	for m in range(initial_iterations):
		it+=1
		temp1=zeros(shape=(p_1,p_1))
		temp=array(temp1,dtype=float)
		for i in range(p_1):
			for j in range(p_1):
				if radial(x[i],y[j])<R: #only points within the circle get updated. All other points outside remain 0 at all times.
					if i==a_1 and j==int(0.5*(p_1-1)):
						temp[j][i]=(1.0-w)*V[j][i]+0.25*w*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]-charge)	
					elif i==b_2 and j==int(0.5*(p_1-1)):
						temp[j][i]=(1.0-w)*V[j][i]+0.25*w*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]+charge)
					else:
						temp[j][i]=(1.0-w)*V[j][i]+0.25*w*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i])
		g=abs((temp-V))
		f=np.max(g)
		list_of_maxima.append(f)
		V=temp  # assigning V to the values in temp in this iteration step 


	while it<10**5 and abs(list_of_maxima[-1])>tolerance:		
		temp1=zeros(shape=(p_1,p_1))
		temp=array(temp1,dtype=float)
		for i in range(p_1):
			for j in range(p_1):
				if radial(x[i],y[j])<R: #only points within the circle get updated. All other points outside remain 0 at all times.
					if i==a_1 and j==int(0.5*(p_1-1)):
						temp[j][i]=(1.0-w)*(V[j][i])+0.25*w*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]-charge)	
					elif i==b_2 and j==int(0.5*(p_1-1)):
						temp[j][i]=(1.0-w)*(V[j][i])+0.25*w*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]+charge)
					else:
						temp[j][i]=(1.0-w)*(V[j][i])+0.25*w*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i])
						
		h=abs((temp-V))
		l=np.max(h)
		list_of_maxima.append(l)
		V=temp  # assigning V to the values in temp in this iteration step
		it+=1 
	iteration[p]=it
	print "the number of iterations required for this run is: %d ." % iteration[p]

#plot(grid,iteration,'r-^')
#xlabel('Number of grid points')
#ylabel('Number of Iterations required')
#title('Plot of number of grid points versus tolerance for the SOR Algorithm')
#show()




