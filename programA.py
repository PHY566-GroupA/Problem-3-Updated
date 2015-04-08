from pylab import *                #importing all functions from pylab
x= arange(-10.0,10.05,0.05)     # array of x,taken till 10.05, to include 10
y=sin (x)                                  # array of sine values of x
z=y/x                                      # array of sinc values of x
plot(x,y,'b-',label='sine')                # plotting the sine values
plot(x,z,'g--',label='sinc')               # plotting the sinc values
ylim(-1.2,1.2)                             # vertical limits of graph
xlim(-10.0,10.05)                          # horizontal limits of graph
xlabel('value of x')                       # label of axis
ylabel('function value')                   # '''''''''''''
legend(loc='lower right')
show()

