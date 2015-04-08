from pylab import *
""" The 1st case is the normal simulation, keeping only the first order term, with time step 1000 years.
    The 2nd case is a simulation run with keeping the second order terms in each stage, also with time step 1000 years.
    The 3rd simulation is the 'exact' simulation, which agrees with the 2nd simulation
"""
nuclei0 = 4.3*(10**(14)) # initial number of nuclei
tau = 8225.00            # approximate decay constant for Carbon
dt_1 = 1000.00           # time step in the 1st case
dt_2 = 1000.00           # time step in the 2nd case
tmax = 20000.00       # maximum time till which simulation runs, in years
n1_steps = int(tmax/dt_1) #number of time steps in the 1st case
n2_steps = int(tmax/dt_2) #number of time steps in the 2nd case

nuclei_1 = [0.0]*n1_steps 
#stores the number of nuclei in the 1st case with time step 1000 years

nuclei_2 = [0.0]*n2_steps
#stores the number of nuclei in the 2nd case with time step 1000 years
t_1 = [0.0]*n1_steps
#time steps for the 1st case 

t_2 = [0.0]*n2_steps
#time steps for the 2nd case

# use Euler's method to integrate equation for radioactive decay

#the first simulation with timestep 1000 years, keeping only first order contribution in each infinitesimal step
t_1[0] = 0.0
nuclei_1[0] = nuclei0
for i in range(n1_steps-1):
    t_1[i+1] = t_1[i]+dt_1    #update the time by the time step unit
    nuclei_1[i+1] = nuclei_1[i]-nuclei_1[i]/tau*(dt_1) #update the number of nuclei



#the second simulation with timestep 1000 years, taking 2nd order contributions in each infinitesimal step
t_2[0] = 0.0
nuclei_2[0] = nuclei0
for i in range(n2_steps-1):
    t_2[i+1] = t_2[i]+dt_2    #update the time by the time step unit
    nuclei_2[i+1] = nuclei_2[i]-nuclei_2[i]/tau*(dt_2) + ((nuclei_2[i])/(2*(tau)**2))*(dt_2)**2  #update the number of nuclei with the 2nd order contribution added

# for the 'exact'plot, choosing an array with timestep 1 year, for even greater accuracy 
q=arange(tmax)

"""
We find the value from the first simulation, at approximately 2 half lives, which is around 11400 years, but for our convenience we take the exact time value to be 11000 years."""

a= nuclei_1[11]  
# the number of nuclei calculated at 17000 years from the 1st case with 1st order contribution only

b= nuclei0*exp(-(11000.0)/tau) 
# the 'exact' number of nuclei at 17000 years

# the percent deviation at 17000 years
print "The percent deviation at 11000 years ( close to 2 half lives, which is exactly 11400 years) is: %(deviation).2f" %{"deviation":((b-a)/b)*100}





# generate figure for the number of nuclei, with logarithmic y axis:    
semilogy(t_1, nuclei_1, 'r-',label="first order contribution")   #1st plot
semilogy(t_2, nuclei_2, 'g-',label="second order contribution")  #2nd plot
semilogy(q,nuclei0*exp(-q/tau),'b--',label="exact plot")         #'exact' plot
xlabel('time(years)')
ylabel('log(number of nuclei)')
title('radioactive decay with time step 1000 years')
legend(loc='lower left')
grid()
show()

activity_1=[x/tau for x in nuclei_1] #activity at each time step in the first plot with first order calculation
activity_2=[y/tau for y in nuclei_2] #activity at each time step in the second plot with second order calculation

# generate normal plot for the activity:
plot(t_1, activity_1, 'r-',label="first order calculation")   #1st plot for the activity with first order calculation
plot(t_2, activity_2, 'g-',label="second order calculation")  #2nd plot for the activity with second order calculation
plot(q,(nuclei0*exp(-q/tau))/tau,'b--',label="exact plot")    #'exact' plot for the activity 
xlabel('time(years)')
ylabel('activity($year^{-1})$')
title('radioactive decay with time step of 1000 years')
legend(loc='upper right')
grid()
show()






