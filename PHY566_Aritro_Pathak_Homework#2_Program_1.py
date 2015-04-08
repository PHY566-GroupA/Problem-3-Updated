from pylab import *

nuclei0 = 4.3*(10**(14)) # initial number of nuclei
tau = 8225.00         # approximate decay constant for Carbon,in years
dt_1 = 10.00          # time step in the 1st case
dt_2 = 100.00         # time step in the 2nd case
tmax = 20000.00       # maximum time till which simulation runs, in years
n1_steps = int(tmax/dt_1) #number of time steps in the 1st case
n2_steps = int(tmax/dt_2) #number of time steps in the 2nd case

nuclei_1 = [0.0]*n1_steps 
#stores the number of nuclei in the 1st case with time step 10 years

nuclei_2 = [0.0]*n2_steps
#stores the number of nuclei in the 2nd case with time step 100 years

t_1 = [0.0]*n1_steps
#time steps for the 1st case 

t_2 = [0.0]*n2_steps
#time steps for the 2nd case


# use Euler's method to integrate equation for radioactive decay

#the first simulation with timestep 10 years
t_1[0] = 0.0
nuclei_1[0] = nuclei0
for i in range(n1_steps-1):
    t_1[i+1] = t_1[i]+dt_1    #update the time by the time step unit
    nuclei_1[i+1] = nuclei_1[i]-nuclei_1[i]/tau*(dt_1) #update the number of nuclei

#the second simulation with timestep 100 years
t_2[0] = 0.0
nuclei_2[0] = nuclei0
for i in range(n2_steps-1):
    t_2[i+1] = t_2[i]+dt_2    #update the time by the time step unit
    nuclei_2[i+1] = nuclei_2[i]-nuclei_2[i]/tau*(dt_2)  #update the number of nuclei

# for the 'exact'plot, choosing an array with timestep 1 year, for even greater accuracy 
q=arange(tmax)

activity_1=[x/tau for x in nuclei_1] #activity at each time step in the first plot with time step 10 years
activity_2=[y/tau for y in nuclei_2] #activity at each time step in the second plot with time step 100 years


# generate figure for the number of nuclei, with logarithmic y axis:    
semilogy(t_1, nuclei_1, 'r-',label="time step->10 years")   #1st plot for the number of nuclei, on semilog scale
semilogy(t_2, nuclei_2, 'g-',label="time step->100 years")  #2nd plot for the number of nuclei, on the semilog scale
semilogy(q,nuclei0*exp(-q/tau),'b--',label="exact plot")    #'exact' plot for the number of nuclei, on the semilog scale
xlabel('time(years)')
ylabel('log(number of nuclei)')
title('radioactive decay')
legend(loc='lower left')
grid()
show()

# generate normal plot for the activity:
plot(t_1, activity_1, 'r-',label="time step->10 years")   #1st plot for the activity with time step of 10 years
plot(t_2, activity_2, 'g-',label="time step->100 years")  #2nd plot for the activity with time step of 100 years
plot(q,(nuclei0*exp(-q/tau))/tau,'b--',label="exact plot")    #'exact' plot for the activity 
xlabel('time(years)')
ylabel('activity($year^{-1})$')
title('radioactive decay')
legend(loc='lower left')
grid()
show()


