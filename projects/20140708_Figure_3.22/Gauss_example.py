#from pylab import *
import warnings
warnings.simplefilter("ignore",DeprecationWarning)
import matplotlib as plt
#plt.use('Agg') #avoid X11 issues.
import scipy, numpy, pylab #, asciidata
from numpy import *
from pylab import *
from scipy import *
from scipy.optimize import leastsq
import pyfits
import os
from scipy import stats
from scipy import interpolate
from scipy.interpolate import interp1d
import itertools
import decimal
from decimal import *
from matplotlib.ticker import NullFormatter
import matplotlib.gridspec as gridspec
import astropy
from astropy.table import Table
import pyfits
from astropy.time import Time
import sys
from astropy.io import ascii


#generate random gauss data
N=input("""number of points ->""")
sigma=10.0
mu=50.0

def gaussian(x):
       return (1/sqrt(2*pi*(sigma**2)))*exp(-(x-mu)**2/(2*sigma**2))

X=arange(0.0,100.0,100.0/N)
Y=gaussian(X)
Z=[.001]*N
C=random.normal(0.0,Z,N)

#print(Z)
Y=Y+C

#print(len(X))
#print(len(Y))
#plot(X,Y)
scatter(X,Y)
errorbar(X,Y,yerr=.001, fmt=None, marker=None, mew=0)

gauss_fit = lambda p, x: (1.0/sqrt(2.0*(3.14)*(p[1]**2)))*exp(-(x-p[0])**2/(2*p[1]**2))# #1d Gaussian func
e_gauss_fit = lambda p, x, y, z: ((gauss_fit(p,x)-y)/z)# #1d Gaussian fit weighted

v0=[mu,sigma] #inital guesses for Gaussian Fit. $just do it around the peak
out = leastsq(e_gauss_fit, v0[:], args=(X, Y, Z), maxfev=100000, full_output=1) #Gauss Fit
v = out[0] #fit parammeters vector
covar = out[1] #covariance matrix output
xxx = arange(min(X),max(X),.01)#(X[1]-X[0])/10)

ccc = gauss_fit(v,xxx)

plot(xxx,ccc,'b-')

s = interpolate.InterpolatedUnivariateSpline(xxx,ccc)


resids=[0.0]*N
resids[0]=0.0
weighted=[0.0]*N
weighted[0]=0.0


for i in range(N-1):
        resids[i]=(Y[i]-s(X[i]))
        weighted[i]=resids[i]**2/Z[i]**2

print "chi squared", sum(weighted)
print "mu: ", v[0]
print "sigma: ", v[1]

print "uncert in mu", ((covar[0][0])**.5)
print "uncert in sigma", ((covar[1][1])**.5)
#print "correlation", ((covar[0][1])**.5)
#print "correlation", ((covar[1][0])**.5)
show()

