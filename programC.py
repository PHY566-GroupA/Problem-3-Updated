from pylab import * 
x,sine,sinc= loadtxt('table.txt',unpack = True) #unpacking from file, into 3 different arrays
plot(x,sine,'r-',label='sine')           #plotting the sine function                
plot(x,sinc,'y--',label='sinc')            #plotting the sinc function
ylim(-1.2,1.2)                            #limits, same as in program 1
xlim(-10.0,10.05)                          #limits, same as in program 1
xlabel('value of x')                       #labels, same as in program 1
ylabel('function value')                 #labels, same as in program 1
legend(loc='upper right') 
show()

