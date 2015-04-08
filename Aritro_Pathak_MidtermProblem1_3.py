from pylab import *

#part c

#number of iterations required for the jacobi algorithm (this is taking a long time with the accuracy value of 5*(10**(-6)), but reasonably quick with 5*(10**(-5))

#There seems to be some bug because of which the code seems to give correct result only for multiple values of 10 in N. Could not run this code by varying the number of grid points in intervals that are not 10. Ran the code for each value of N differently. Each value of N is put in the trivial array named grid, below

initial_iterations=30   # the number of iterations after which the convergence criterion should be applied, to avoid a possible false convergence
charge=1.0 # (Q/epsilon_{0})*(unit grid area)
R=10 #radius
grid=linspace(130,130,1) #only one value for the number density is chosen. I manually ran the code multiple times to find the result. The print statement in the end gives the iteration value for each run. Only multiples of 10 seem to work here
iterations1=zeros(1)
iteration=array(iterations1,dtype=float)
tolerance= 5*(10**(-6))

def radial(a,b):
	var1=sqrt(a*a+b*b)
	return var1

def distance1(a,b):
	var2=sqrt((a+0.3)**2+b**2)
	return var2

def distance2(a,b):
	var3=sqrt((a-0.3)**2+b**2)
	return var3

for p in range(len(grid)):
	p_1=int(grid[p])
	x=linspace(-R,R,p_1)
	y=linspace(-R,R,p_1)
	V1=zeros(shape=(p_1,p_1))
	V=array(V1,dtype=float)    #initialising the potential to 0, initially.... The first coordinate of V gives the y coordinate and the 2nd coordinate gives the x coordinate. This is done so because later while doingthe contour plot, meshgrid does exactly the same thing with its grid.
	for i in range(p_1):
		if x[i]<-0.3 and x[i+1]>-0.3:
			a_1=i        # we will put the negative charge at -0.3 
			a_2=(i+1)   
		if x[i]<0.3 and x[i+1]>0.3:
			b_1=i        
			b_2=(i+1)    # we will put the positive charge at +0.3
	initial_max=0.0	
	list_of_maxima=[]  #will store all the maximum difference between successive steps, here
	list_of_maxima.append(initial_max)
	it=0
	for m in range(initial_iterations):  #initial number of iterations where no 
		it+=1
		temp1=zeros(shape=(p_1,p_1))
		temp=array(temp1,dtype=float)
		for i in range(p_1):
			for j in range(p_1):
				if radial(x[i],y[j])<R: #only points within the circle get updated. All other points outside remain 0 at all times.
					if i==a_1 and j==int(0.5*(p_1-1)):
						temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]-charge)	
					elif i==b_2 and j==int(0.5*(p_1-1)):
						temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]+charge)
					else:
						temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i])
		g=abs((temp-V))
		f=np.max(g)
		list_of_maxima.append(f)  
		V=temp  # assigning V to the values in temp in this iteration step 
#	print 'y' #comes here all right
#	print it
	while it< 10**6:
		if abs(list_of_maxima[-1])>tolerance:	
#			if p>1:
#				print 'z' #checking if it enters from the 3rd run onwards	
			temp1=zeros(shape=(p_1,p_1))
			temp=array(temp1,dtype=float)
			for i in range(p_1):
				for j in range(p_1):
					if radial(x[i],y[j])<R: #only points within the circle get updated. All other points outside remain 0 at all times.
						if i==a_1 and j==int(0.5*(p_1-1)):
							temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]-charge)	
						elif i==b_2 and j==int(0.5*(p_1-1)):
							temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i]+charge)
						else:
							temp[j][i]=0.25*(V[j][i+1]+ V[j][i-1]+ V[j-1][i]+ V[j+1][i])
			h=abs((temp-V))
			l=np.max(h)
			list_of_maxima.append(l)
			V=temp  # assigning V to the values in temp in this iteration step 
			it+=1
		else:
			break
	iteration[p]=it
	print "the number of iterations required for this run is: %d ." % iteration[p]

#plot(grid,iteration,'r-^')
#xlabel('Number of grid points')
#ylabel('Number of Iterations required')
#title('Plot of number of grid points versus tolerance for the Jacobi Algorithm')
#show()




