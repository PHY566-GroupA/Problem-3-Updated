from pylab import *
x= arange(-10.0,10.05,0.05)   #the arrays 
y= sin (x)                     #the arrays             
z= y/x                         #the arrays
u= len(x)                      #length of the array stored in the variable u
file=open('table.txt','w')     #creating the file named table.txt
file.write("# x\t\tsin(x)\t\tsinc(x)\n\n")             #writing to this file
a=0
while a < u :
      file.write("%2.3f\t\t %2.3f\t\t %2.3f\n" %(x[a],y[a],z[a])) #writing to the file
      a+=1
file.close() #close file
