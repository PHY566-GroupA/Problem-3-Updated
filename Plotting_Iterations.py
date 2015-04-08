from pylab import *

density=[60,70,80,90,100,110,120]

#tolearance for the Jacobi algorithm:5*(10^(-5))
iterations_Jacobi=[1589,1905,2197,2457,2680,2853,2985]

#tolerance for the SOR method: 5*(10^(-6))
iterations_SOR=[1219,1359,1444,1482,1494,2088,2097]

plot(density,iterations_Jacobi,'r-^')
xlabel('Number of grid points in either x or y direction')
ylabel('Iterations')
title('Variation of Iterations with grid density in Jacobi algorithm')
grid()
show()

plot(density,iterations_SOR,'r-^')
xlabel('Number of grid points in either x or y direction')
ylabel('Iterations')
title('Variation of Iterations with grid density in SOR algorithm')
grid()
show()
