# M. DeCesar
# Script to read and plot the sample "mystery" dataset
# For UWM python class, 2014 July 22
import numpy as np
from matplotlib import pyplot as plt

#--------------------------------------------
# Open and read data file
#infile = open('data01_14Jul22.dat','r')
infile = open('data02_14Jul22_1Hzpulse.dat','r')
lines = infile.readlines()
infile.close()

#--------------------------------------------
# Assign values to data array
data = np.zeros(len(lines))
for i in range(0,len(lines)):
    line = lines[i].strip('\n')
    data[i] = float(line)

#----------------------------------------
# Plot the data to see what it looks like, and save to a figure

x = np.linspace(1,len(data),num=len(data))
## Examine x if desired
# print x[0],x[len(x)-1]
# print len(x)

plt.figure()
plt.plot(x,data)
plt.xlabel('Data Bin')
plt.ylabel('Data Value')
plt.title('Sample Values from a Normal Distribution')
## Save .png figure if desired:
# plt.savefig('data01_14Jul22')
# plt.savefig('data02_14Jul22_1Hzpulse')
plt.show()

#----------------------------------------
# Print the mean and standard deviation derived from the data
print 'Data mean = %.4f'%np.mean(data)
print 'Data standard deviation = %.4f'%np.std(data)
