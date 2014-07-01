import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


##Generate a gaussian distribution with 500 random numbers and saving  data set to text file

dist=stats.norm(0,2)
r1=dist.rvs(500)
np.savetxt('gauss.txt',r1,fmt='%1.7f')

#Calculating mean,variance,skew,kurtosis,mode of distribution

print "mean=",r1.mean()
print "variance=",r1.var()
print "standard deviation=",np.sqrt(r1.var())
print "skew=",stats.skew(r1)
print "kurtosis=",stats.kurtosis(r1)
print "mode=",stats.mode(r1),"\n"

#plotting the guassian distribution
r1.sort()
p=dist.pdf(r1)
ax=plt.axes()
ax.plot(r1,p)
ax.set_xlabel('x')
ax.set_ylabel('p(x|0,2)')
ax.set_title('Gaussian distribution')
plt.show()

#Plotting the histogram of guassian distribution
ax1=plt.hist(r1,bins=30,facecolor='blue')


#show all the plots
plt.show()

## Calculating the Guass error function

from scipy.special import erf 
print "Guass Error function value=",erf(1)

