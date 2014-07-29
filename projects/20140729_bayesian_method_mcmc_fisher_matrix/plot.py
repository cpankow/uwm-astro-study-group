from matplotlib import pylab as plt
import matplotlib
import numpy
import numpy as np
from scipy.optimize import curve_fit
import pylab as plb  

observeddata = np.loadtxt('orbit_obsv_data')
a = 1000
e = 0.1
nBins = len(observeddata)

magnify = 1e2
whichparam = 1
msigmaarray = np.array([1e-1, 1e-4])  
meanarray = np.array([a, e])
sigma = msigmaarray[whichparam]
mean = meanarray[whichparam]
datamcmcsampler = plb.loadtxt('samplerFlatChain.txt') 
paramsampler = datamcmcsampler[:,whichparam]
datalike = np.loadtxt("parameterLnprob.txt")
prob = np.exp(datalike[:,-1])
param = datalike[:,whichparam]


def gaussian(x, *p):
    A, mu, sigma = p
    return A*numpy.exp(-(x-mu)**2/(2.0*sigma**2))

def gaussian_norm(x, *p):
    mu, sigma = p
    return 1.0/numpy.sqrt(2*np.pi*sigma*sigma)*numpy.exp(-(x-mu)**2/(2.*sigma**2))


param_fisher = np.linspace(mean-4*sigma, mean+4*sigma, 300)
amp =  (np.sqrt(2*np.pi)*sigma)**(-1)
likelihood_fisher = amp * np.exp(-0.5*(param_fisher-mean)**2/(sigma**2))

list_sort = param.argsort()
sorted_param = param[list_sort]
sorted_prob = prob[list_sort]

param = sorted_param

hist, bin_edges = numpy.histogram(paramsampler, bins=nBins, density=True)
bin_centres = ((bin_edges[:-1] + bin_edges[1:])/2-mean)
bin_centres = bin_centres

p0 = [amp, 0.0, sigma]
coeff, var_matrix = curve_fit(gaussian, bin_centres, hist, p0=p0)
coeff[0] = (np.sqrt(2*np.pi)*coeff[2])**(-1)
coeff[1] = coeff[1]
coeff[2] = coeff[2]
print coeff, sigma
hist_fit = gaussian((param-mean), *coeff)
bin_centres = bin_centres

area2 = 0.0
for k in np.arange(1, len(param)):
	area2 = area2 + (param[k]-param[k-1])*gaussian((param[k]-mean),*coeff)
	
print "area2", area2
nSkip = 20
matplotlib.rcParams.update({'font.size':26})
plt.plot(bin_centres, hist*area2, 'g', linewidth = 2.1, label='MCMC samples')
plt.plot(param - mean, hist_fit, 'm-', linewidth = 3.8, label='Fit to samples')
#plt.plot(param_fisher - mean, likelihood_fisher, 'b-', linewidth = 3.5, label = 'Fisher matrix')

plt.legend(loc=1, prop={'size':20})
plt.xlabel("parameter - {0:6.2f}".format(mean), fontsize=26)
plt.ylabel("Probability", fontsize=26)
plt.xlim(-7*sigma,7*sigma)
plt.show()


