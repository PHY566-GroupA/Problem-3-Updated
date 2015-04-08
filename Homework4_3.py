from pylab import *

mass=1.0  #the mass has not been mentiond anywhere, I take it to be a unit mass.
g=9.8
l=9.8
#taking g/l to be 1 everywhere
gamma=0.25
alpha_D=0.5    #the amplitude of the driving force     
#alpha_D=1.2      # LYAPUNOV CONSTANT only extractable for values of alpha_D 0.5 and 0.2. change the values from here. In these cases the motion is still almost sinusoidal,and hence not chaotic. it is chaotic for alpha_D=1.2 but in that case the Lyapunov exponent is not clear.
dt=0.01          # differential time step
t_max=100.00     # we can change t_max(in seconds) here and no change is needed in the rest of the code
total_steps=int(t_max/dt)   #total number of time steps,10000




time=[0.0]*total_steps
theta1=[0.0]*total_steps
omega1=[0.0]*total_steps
theta2=[0.0]*total_steps
omega2=[0.0]*total_steps
theta3=[0.0]*total_steps
omega3=[0.0]*total_steps
d_theta=[0.0]*total_steps  #this is actually the difference of thetas
log_d_theta=[0.0]*total_steps  #this is the logarithm of the difference of thetas
constant=[0.0]*total_steps
constant_nonzero=[]
#omega_D=0.95      #if the driving frequency is taken close to the resonant frequency , then the result is still approximately sinusoidal, when the non linear term sin(theta) is taken in the force in place of theta
omega_D=0.666    # when driving frequency is lowered to this value, the chaotic behaviour sets in.
theta1[0]=2.000      #INTIAL THETA FOR THE FIRST CASE
omega1[0]=0.0      #initial \omega
theta2[0]=2.001    #INTIAL THETA FOR THE SECOND CASE IS SLIGHTLY DIFFERENT
omega2[0]=0.0
theta3[0]=2.102    #INTIAL THETA FOR THE THIRD CASE IS AGAIN SLIGHTLY DIFFERENT
omega3[0]=0.0
time[0]= 0.000      

for i in range(total_steps-1):

#first calculation
	k_1=dt*omega1[i]
	l_1=dt*(-sin(theta1[i])-2*gamma*omega1[i]+alpha_D*sin(omega_D*time[i])) #replacing theta by sin(theta)
	k_2=dt*(omega1[i] + 0.5*l_1) 
	l_2=dt*(-sin(theta1[i]+0.5*k_1)-2*gamma*(omega1[i]+0.5*l_1)+alpha_D*sin(omega_D*(time[i]     +0.50*dt)))#theta replaced by sin(theta)
	k_3=dt*(omega1[i] + 0.5*k_2)
	l_3=dt*(-sin(theta1[i]+0.5*k_2)-2*gamma*(omega1[i]+0.5*l_2)+alpha_D*sin(omega_D*(time[i]+0.50*dt)))#theta replaced by sin(theta)
	k_4=dt*(omega1[i] + k_3)
	l_4=dt*(-sin(theta1[i]+k_3)-2*gamma*(omega1[i]+l_3)+alpha_D*sin(omega_D*(time[i]+dt))) #theta replaced by sin(theta)

	time[i+1]= time[i] + dt     #updating time
	theta1[i+1]=theta1[i] + (1.0/6.0)*(k_1+2*k_2+2*k_3+k_4) #updating \theta
	if theta1[i+1]> pi:
		theta1[i+1]=theta1[i+1]-2*pi
	if theta1[i+1]< -pi:
		theta1[i+1]=theta1[i+1]+2*pi
	omega1[i+1]=omega1[i] + (1.0/6.0)*(l_1+2*l_2+2*l_3+l_4) #updating \omega


#second calculation
	k_1=dt*omega2[i]
	l_1=dt*(-sin(theta2[i])-2*gamma*omega2[i]+alpha_D*sin(omega_D*time[i])) #replacing theta by sin(theta)
	k_2=dt*(omega2[i] + 0.5*l_1) 
	l_2=dt*(-sin(theta2[i]+0.5*k_1)-2*gamma*(omega2[i]+0.5*l_1)+alpha_D*sin(omega_D*(time[i]     +0.50*dt)))#theta replaced by sin(theta)
	k_3=dt*(omega2[i] + 0.5*k_2)
	l_3=dt*(-sin(theta2[i]+0.5*k_2)-2*gamma*(omega2[i]+0.5*l_2)+alpha_D*sin(omega_D*(time[i]+0.50*dt)))#theta replaced by sin(theta)
	k_4=dt*(omega2[i] + k_3)
	l_4=dt*(-sin(theta2[i]+k_3)-2*gamma*(omega2[i]+l_3)+alpha_D*sin(omega_D*(time[i]+dt))) #theta replaced by sin(theta)

	time[i+1]= time[i] + dt     #updating time
	theta2[i+1]=theta2[i] + (1.0/6.0)*(k_1+2*k_2+2*k_3+k_4) #updating \theta
	if theta2[i+1]> pi:  #keeping the angle between +pi and -pi, the dynamical equations of motion remain unchanged for the sinusoidal force
		theta2[i+1]=theta2[i+1]-2*pi
	if theta2[i+1]< -pi:
		theta2[i+1]=theta2[i+1]+2*pi
	omega2[i+1]=omega2[i] + (1.0/6.0)*(l_1+2*l_2+2*l_3+l_4) #updating \omega


#third calculation
	k_1=dt*omega3[i]
	l_1=dt*(-sin(theta3[i])-2*gamma*omega3[i]+alpha_D*sin(omega_D*time[i])) #replacing theta by sin(theta)
	k_2=dt*(omega3[i] + 0.5*l_1) 
	l_2=dt*(-sin(theta3[i]+0.5*k_1)-2*gamma*(omega3[i]+0.5*l_1)+alpha_D*sin(omega_D*(time[i]     +0.50*dt)))#theta replaced by sin(theta)
	k_3=dt*(omega3[i] + 0.5*k_2)
	l_3=dt*(-sin(theta3[i]+0.5*k_2)-2*gamma*(omega3[i]+0.5*l_2)+alpha_D*sin(omega_D*(time[i]+0.50*dt)))#theta replaced by sin(theta)
	k_4=dt*(omega3[i] + k_3)
	l_4=dt*(-sin(theta3[i]+k_3)-2*gamma*(omega3[i]+l_3)+alpha_D*sin(omega_D*(time[i]+dt))) #theta replaced by sin(theta)

	time[i+1]= time[i] + dt     #updating time
	theta3[i+1]=theta3[i] + (1.0/6.0)*(k_1+2*k_2+2*k_3+k_4) #updating \theta
	if theta3[i+1]> pi:
		theta3[i+1]=theta3[i+1]-2*pi
	if theta3[i+1]< -pi:
		theta3[i+1]=theta3[i+1]+2*pi
	omega3[i+1]=omega3[i] + (1.0/6.0)*(l_1+2*l_2+2*l_3+l_4) #updating \omega



#calculating for the lyapunov exponent:
	d_theta[i+1]=theta1[i+1]-theta2[i+1]
	log_d_theta[i+1]=log(abs(d_theta[i+1]))
	if i>9000:	#after 9000 time steps, the value for the lyapunov constant seems to converge
		constant[i+1]=(log_d_theta[i+1])/(time[i+1])  # each of the non zero values in this array should be approximately equal to the Lyapunov constant.
		constant_nonzero.append(constant[i+1])

A=sum(constant_nonzero)
B=len(constant_nonzero)
C=abs(A/B) #this average is taken as the Lyapunov constant
print "the Lyapunov constant is: %.3f (in units of inverse second)" %C


plot(time,theta1)
xlabel('time(t) (seconds)')
ylabel('$\\theta(t)|$')
title('$\\theta(t) vs time(t) for $\\alpha_{D}=1.2$')
grid()
show()

#plot(time,omega1,'r-')    #can use this to separately check for the solution with the Runge Kutta
#ylabel('angular velocity')
#xlabel('time')
#title("omega vs time:non linear force,$\\alpha_{D}=0.2, \\Omega_{D}=0.95$")
#grid()
#show()

#plot(time,theta1,'r-')    #can use this to separately check for the solution with the Runge Kutta
#ylabel('theta')
#xlabel('time')
#title("theta vs time:non linear force, $\\alpha_{D}=0.2 \\Omega_{D}=0.95$")
#grid()
#show()
	




































